from datetime import date, datetime
from pydantic import BaseModel

class StatsBase(BaseModel):
    streak: int
    solved_in: int
    date: datetime

class StatsCreate(StatsBase):
    pass

class Stats(StatsBase):
    id: int
    user_id: str

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    user: str
    email:str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str
    stats: list[Stats] = []

    class Config:
        orm_mode = True