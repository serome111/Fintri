from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey, DateTime, Enum as PG_ENUM
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.db.database import Base

class TypeEnum(enum.Enum):
    gasto = "gasto"
    ahorro = "ahorro"
    ingreso = "ingreso"

class Type3Enum(enum.Enum):
    fijo = "fijo"
    variable = "variable"

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    article = Column(String, nullable=False)
    date = Column(Date, nullable=True)
    value = Column(DECIMAL(15, 2), nullable=False)
    type = Column(PG_ENUM(TypeEnum), nullable=False)
    type2 = Column(String, nullable=True)
    type3 = Column(PG_ENUM(Type3Enum), nullable=False)
    status = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="transactions")
    created_at = Column(DateTime, default=datetime.utcnow)

class FixedTransaction(Base):
    __tablename__ = "fixed_transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    article = Column(String, nullable=False)
    value = Column(DECIMAL(15, 2), nullable=False)
    type = Column(PG_ENUM(TypeEnum), nullable=False)
    type2 = Column(String, nullable=True)
    type3 = Column(PG_ENUM(Type3Enum), nullable=False)
    status = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="fixed_transactions")
    created_at = Column(DateTime, default=datetime.utcnow)

class CDT(Base):
    __tablename__ = "cdt"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    initial_amount = Column(DECIMAL(15, 2), nullable=False)
    interest_rate = Column(DECIMAL(5, 2), nullable=False)
    start_date = Column(Date, nullable=False)
    duration_months = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="cdts")
    accumulated_interests = relationship("AccumulatedInterest", back_populates="cdt")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Fiducuenta(Base):
    __tablename__ = "fiducuenta"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    current_balance = Column(DECIMAL(15, 2), nullable=False)
    interest_rate = Column(DECIMAL(5, 2), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="fiducuentes")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class AccumulatedInterest(Base):
    __tablename__ = "accumulated_interests"
    
    id = Column(Integer, primary_key=True, index=True)
    cdt_id = Column(Integer, ForeignKey('cdt.id'), nullable=False)
    date = Column(Date, nullable=False)
    accumulated_interest = Column(DECIMAL(15, 2), nullable=False)
    cdt = relationship("CDT", back_populates="accumulated_interests")
    created_at = Column(DateTime, default=datetime.utcnow)
