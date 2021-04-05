from datetime import date
from typing import List

from pydantic import BaseModel

class UserBase(BaseModel):
    nickname: str


class UserCreate(UserBase):
    password: str


class UserShow(UserBase):
    id: int = None
    is_active: bool


class User(UserShow):
    hashed_password: str
    role: str

    class Config:
        orm_mode = True