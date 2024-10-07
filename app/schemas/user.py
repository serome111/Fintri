from pydantic import BaseModel
from typing import List
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    roles: List[str] = ["user"]

class User(UserBase):
    id: int
    roles: List[str]

    class Config:
        orm_mode = True
