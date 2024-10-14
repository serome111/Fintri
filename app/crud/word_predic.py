from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.word_predic import WordPredic
from app.models.transaction import TypeEnum
from sqlalchemy.exc import SQLAlchemyError,IntegrityError


# Crear una nueva palabra
def create_palabra(db: Session, palabra: str, categoria: TypeEnum):
    
    palabra_existente = db.query(WordPredic).filter(WordPredic.palabra == palabra).first()
    if palabra_existente:
        raise HTTPException(status_code=400, detail="La palabra ya existe.")

    try:
        nueva_palabra = WordPredic(palabra=palabra, categoria=categoria)
        db.add(nueva_palabra)
        db.commit()
        db.refresh(nueva_palabra)
        return nueva_palabra
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Violación de integridad. La palabra ya existe o hay un conflicto.")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al insertar palabra en la base de datos.")

# Obtener todas las palabras o filtrar por categoría
def get_palabras(db: Session, categoria: TypeEnum = None, skip: int = 0, limit: int = 10):
    try:
        query = db.query(WordPredic)
        if categoria:
            query = query.filter(WordPredic.categoria == categoria)
        return query.offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al obtener palabras: " + str(e))


# Obtener una palabra por ID
def get_palabra(db: Session, palabra_id: int):
    try:
        palabra = db.query(WordPredic).filter(WordPredic.id == palabra_id).first()
        if not palabra:
            raise HTTPException(status_code=404, detail="Palabra no encontrada")
        return palabra
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error de base de datos: " + str(e))


# Actualizar una palabra existente
def update_palabra(db: Session, palabra_id: int, nueva_palabra: str = None, nueva_categoria: TypeEnum = None):
    try:
        palabra = db.query(WordPredic).filter(WordPredic.id == palabra_id).first()
        if not palabra:
            raise HTTPException(status_code=404, detail="Palabra no encontrada")

        if nueva_palabra:
            palabra.palabra = nueva_palabra
        if nueva_categoria:
            palabra.categoria = nueva_categoria

        db.commit()
        db.refresh(palabra)
        return palabra
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al actualizar palabra: " + str(e))

# Eliminar una palabra
def delete_palabra(db: Session, palabra_id: int):
    try:
        palabra = db.query(WordPredic).filter(WordPredic.id == palabra_id).first()
        if not palabra:
            raise HTTPException(status_code=404, detail="Palabra no encontrada")

        db.delete(palabra)
        db.commit()
        return {"message": "Palabra eliminada con éxito"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al eliminar palabra: " + str(e))
