from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError 
from sqlalchemy import func, extract
from app.models.transaction import Transaction as TransactionModel, FixedTransaction as FixedTransactionModel, TypeEnum
from app.schemas.transaction import TransactionCreate, TransactionUpdate
from fastapi import HTTPException
from datetime import datetime, date
import logging

logger = logging.getLogger(__name__)

def create_transaction(db: Session, transaction: TransactionCreate, user_id: int):
    try:
        logger.debug("Creating transaction for user_id: %s", user_id)
        transaction_data = transaction.dict(exclude_unset=True)
        transaction_data.pop('user_id', None)

        db_transaction = TransactionModel(**transaction_data, user_id=user_id)
        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)

        if transaction.type2 == "fixed":
            db_transaction_fixed = FixedTransactionModel(**transaction_data, user_id=user_id)
            db.add(db_transaction_fixed)
            db.commit()
            db.refresh(db_transaction_fixed)
            return db_transaction_fixed

        return db_transaction

    except SQLAlchemyError as e:
        db.rollback()
        logger.error("Database error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error de base de datos: " + str(e))
    except Exception as e:
        db.rollback()
        logger.exception("Unknown error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error desconocido: " + str(e))



def get_transactions(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    try:
        logger.debug("Fetching transactions for user_id: %s", user_id)
        return db.query(TransactionModel).filter(TransactionModel.user_id == user_id).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error("Database error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error de base de datos: " + str(e))
    except Exception as e:
        logger.error("Unknown error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error desconocido: " + str(e))


def get_transaction(db: Session, transaction_id: int, user_id: int):
    try:
        logger.debug("Fetching transaction with id: %s for user_id: %s", transaction_id, user_id)
        return db.query(TransactionModel).filter(TransactionModel.id == transaction_id, TransactionModel.user_id == user_id).first()
    except SQLAlchemyError as e:
        logger.error("Database error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error de base de datos: " + str(e))
    except Exception as e:
        logger.error("Unknown error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error desconocido: " + str(e))


def update_transaction(db: Session, db_transaction: TransactionModel, transaction_update: TransactionUpdate):
    try:
        logger.debug("Updating transaction with id: %s", db_transaction.id)
        update_data = transaction_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_transaction, key, value)
        db.commit()
        db.refresh(db_transaction)
        return db_transaction
    except SQLAlchemyError as e:
        db.rollback()
        logger.error("Database error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error de base de datos: " + str(e))
    except Exception as e:
        db.rollback()
        logger.exception("Unknown error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error desconocido: " + str(e))


def get_sum_by_type(db: Session, user_id: int, month: int = None):
    try:
        logger.debug("Summing transaction values for user_id: %s", user_id)
        query_filters = [TransactionModel.user_id == user_id]

        if month:
            query_filters.append(extract('month', TransactionModel.date) == month)

        sum_gasto = db.query(func.sum(TransactionModel.value)).filter(
            *query_filters,
            TransactionModel.type == TypeEnum.gasto.value
        ).scalar() or 0
        sum_ahorro = db.query(func.sum(TransactionModel.value)).filter(
            *query_filters,
            TransactionModel.type == TypeEnum.ahorro.value
        ).scalar() or 0
        sum_ingreso = db.query(func.sum(TransactionModel.value)).filter(
            *query_filters,
            TransactionModel.type == TypeEnum.ingreso.value
        ).scalar() or 0

        return {
            "sum_gasto": sum_gasto,
            "sum_ahorro": sum_ahorro,
            "sum_ingreso": sum_ingreso,
            "sum_efectivo":sum_ingreso-sum_gasto,
            "billetera": sum_ingreso-sum_gasto-sum_ahorro #lo que tengo para gastar o invertir
        }
    except SQLAlchemyError as e:
        logger.error("Database error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error de base de datos: " + str(e))
    except Exception as e:
        logger.error("Unknown error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error desconocido: " + str(e))


def update_fixed_transactions(db: Session):
    try:
        logger.debug("Updating fixed transactions")
        fixed_transactions = db.query(FixedTransactionModel).all()
        for transaction_fixed in fixed_transactions:
            new_transaction = TransactionModel(
                article=transaction_fixed.article,
                date=datetime.now().date(),
                value=transaction_fixed.value,
                type=transaction_fixed.type,
                type2=transaction_fixed.type2,
                type3=transaction_fixed.type3,
                status=transaction_fixed.status,
                user_id=transaction_fixed.user_id
            )
            db.add(new_transaction)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error("Database error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error de base de datos: " + str(e))
    except Exception as e:
        db.rollback()
        logger.exception("Unknown error: %s", str(e))
        raise HTTPException(status_code=500, detail="Error desconocido: " + str(e))
