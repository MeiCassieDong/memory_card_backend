from typing import List, Union

from pydantic import BaseModel


class PairsBase(BaseModel):
    cardA: str
    cardB: Union[str, None] = None


class PairsCreate(PairsBase):
    pass


class Pairs(PairsBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    cards: List[Pairs] = []

    class Config:
        orm_mode = True