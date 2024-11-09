from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    roles = Column(ARRAY(String), default=["user"])
    transactions = relationship("Transaction", back_populates="user")
    fixed_transactions = relationship("FixedTransaction", back_populates="user")
    cdts = relationship("CDT", back_populates="user")
    fiducuentes = relationship("Fiducuenta", back_populates="user")
