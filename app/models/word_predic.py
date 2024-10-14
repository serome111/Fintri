from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from app.models.transaction import TypeEnum  # Importa el enum TypeEnum
from app.db.database import Base

class WordPredic(Base):
    __tablename__ = 'palabras'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    palabra = Column(String(255), nullable=False, unique=True)
    categoria = Column(Enum(TypeEnum), nullable=False)