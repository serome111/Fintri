from pydantic import BaseModel, field_validator
from typing import Optional
import datetime
from app.models.transaction import TypeEnum,Type3Enum

class TransactionCreate(BaseModel):
    article: str
    date: datetime.date
    value: float
    type: TypeEnum
    type2: str
    type3:Type3Enum
    status: int

class TransactionUpdate(BaseModel):
    article: str | None = None
    date: datetime.date | None = None
    value: float | None = None
    type: TypeEnum | None = None
    type2: str | None = None
    type3: Type3Enum | None = None
    status: int | None = None

    @field_validator('date', mode='before')
    def check_date_format(cls, v):
        if v is None or isinstance(v, datetime.date):
            return v
        if isinstance(v, str):
            try:
                return datetime.date.fromisoformat(v)
            except ValueError:
                raise ValueError("Formato de fecha inválido. Se espera YYYY-MM-DD.")
        raise TypeError("Tipo de dato inválido para el campo 'date'.")

class Transaction(BaseModel):
    id: int
    article: str
    date: datetime.date
    value: float
    type: str
    type2: str
    type2: str
    status: int

    class Config:
        from_attributes = True
