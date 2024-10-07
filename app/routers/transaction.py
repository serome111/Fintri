from fastapi import APIRouter, HTTPException, Depends,Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func
from app.schemas.transaction import TransactionCreate, Transaction, TransactionUpdate
from app.crud import transaction as crud_transaction
from app.db.database import get_db
from app.core.security import get_current_user, get_current_user_roles
from app.models.transaction import Transaction as TransactionModel
from app.models.user import User
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/transactions/", response_model=Transaction)
def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    logger.debug("Request to create transaction for user_id: %s", current_user.id)
    try:
        return crud_transaction.create_transaction(db, transaction, user_id=current_user.id)
    except HTTPException as e:
        logger.error("HTTP exception: %s", e.detail)
        raise
    except Exception as e:
        logger.exception("Unknown error during transaction creation: %s", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")



@router.get("/transactions/", response_model=list[Transaction])
def read_transactions(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    logger.debug("Request to read transactions for user_id: %s", current_user.id)
    if "admin" in current_user.roles:
        try:
            transactions = db.query(TransactionModel).offset(skip).limit(limit).all()
            logger.debug("Fetched transactions for admin user")
        except SQLAlchemyError as e:
            logger.error("Database error: %s", str(e))
            raise HTTPException(status_code=500, detail="Error de base de datos: " + str(e))
        except Exception as e:
            logger.error("Unknown error: %s", str(e))
            raise HTTPException(status_code=500, detail="Error desconocido: " + str(e))
    else:
        transactions = crud_transaction.get_transactions(db, user_id=current_user.id, skip=skip, limit=limit)
        logger.debug("Fetched transactions for normal user")
    return transactions


@router.put("/transactions/{transaction_id}", response_model=Transaction)
def update_transaction(
    transaction_id: int,
    transaction: TransactionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    logger.debug("Request to update transaction for user_id: %s", current_user.id)
    db_transaction = crud_transaction.get_transaction(db, transaction_id=transaction_id, user_id=current_user.id)
    # db_transaction = crud_transaction.get_transactions(db, transaction_id=transaction_id, user_id=current_user.id)
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    update_data = transaction.dict(exclude_unset=True)
    print(transaction.dict())
    print(update_data)
    for key, value in update_data.items():
        setattr(db_transaction, key, value)

    try:
        db.commit()
        db.refresh(db_transaction)
        return db_transaction
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")

    # return crud_transaction.update_transaction(db, db_transaction, transaction)


@router.get("/transactions/sum_by_type")
def sum_by_type(
    month: int = Query(None, ge=1, le=12),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    logger.debug("Request to sum transactions for user_id: %s", current_user.id)
    return crud_transaction.get_sum_by_type(db, user_id=current_user.id, month=month)    
