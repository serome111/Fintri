from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.schemas.word_predic import PalabraCreate, PalabraUpdate, WordPredic as WordPredicSchema, PredictionInput
from app.crud import word_predic as crud_word_predic
from app.db.database import get_db
from app.core.security import get_current_user
from app.models.word_predic import WordPredic
from app.models.user import User

import logging

logger = logging.getLogger(__name__)

router = APIRouter()

# Endpoint para crear una nueva palabra
@router.post("/word/", response_model=WordPredicSchema)
def create_palabra(
    palabra_data: PalabraCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    logger.debug("Request to create palabra by user_id: %s", current_user.id)
    try:
        palabra = crud_word_predic.create_palabra(db, palabra_data.palabra, palabra_data.categoria)
        return palabra
    except HTTPException as e:
        logger.error("HTTP exception: %s", e.detail)
        raise
    except Exception as e:
        logger.exception("Unknown error during palabra creation: %s", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")


# Endpoint para obtener las palabras (con opción de filtro por categoría)
@router.get("/word/", response_model=list[WordPredicSchema])
def read_palabras(
    categoria: str = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    logger.debug("Request to read palabras for user_id: %s", current_user.id)
    try:
        palabras = crud_word_predic.get_palabras(db, categoria=categoria, skip=skip, limit=limit)
        return palabras
    except SQLAlchemyError as e:
        logger.error("Database error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error de base de datos: " + str(e))
    except Exception as e:
        logger.error("Unknown error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error desconocido: " + str(e))


# Endpoint para actualizar una palabra existente
@router.put("/word/{palabra_id}", response_model=WordPredicSchema)
def update_palabra(
    palabra_id: int,
    palabra_data: PalabraUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    logger.debug("Request to update palabra for user_id: %s", current_user.id)
    
    # Utiliza la función get_palabra del CRUD para obtener la palabra
    palabra = crud_word_predic.get_palabra(db, palabra_id=palabra_id)

    update_data = palabra_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(palabra, key, value)

    try:
        db.commit()
        db.refresh(palabra)
        return palabra
    except SQLAlchemyError as e:
        db.rollback()
        logger.error("Database error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error de base de datos")
    except Exception as e:
        db.rollback()
        logger.exception("Unknown error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error interno del servidor")


# Endpoint para eliminar una palabra
@router.delete("/word/{palabra_id}")
def delete_palabra(
    palabra_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    logger.debug("Request to delete palabra for user_id: %s", current_user.id)
    palabra = crud_word_predic.get_palabra(db, palabra_id=palabra_id)
    if not palabra:
        raise HTTPException(status_code=404, detail="Palabra no encontrada")

    try:
        crud_word_predic.delete_palabra(db, palabra_id=palabra_id)
        return {"message": "Palabra eliminada con éxito"}
    except SQLAlchemyError as e:
        db.rollback()
        logger.error("Database error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error de base de datos")
    except Exception as e:
        db.rollback()
        logger.exception("Unknown error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error interno del servidor")


# Endpoint para hacer una predicción basada en una palabra
@router.post("/predict/")
def predict(
    input_data: PredictionInput,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    logger.debug("Request to predict based on input: %s by user_id: %s", input_data.input_data, current_user.id)
    words = input_data.input_data.lower().split()

    for word in words:
        palabra_obj = db.query(WordPredic).filter(WordPredic.palabra == word).first()
        if palabra_obj:
            return {"prediction": palabra_obj.categoria.value}

    return {"prediction": "No se encontró ninguna coincidencia"}

