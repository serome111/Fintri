from pydantic import BaseModel
from typing import Optional 
from app.models.transaction import TypeEnum, Type3Enum


class PalabraCreate(BaseModel):
    palabra: str
    categoria: TypeEnum


class PalabraUpdate(BaseModel):
    palabra: Optional[str] = None
    categoria: Optional[TypeEnum] = None


class WordPredicBase(BaseModel):
    palabra: str
    categoria: TypeEnum


class PredictionInput(BaseModel):
    input_data: str


class WordPredic(WordPredicBase):
    id: int

    class Config:
        from_attributes = True
