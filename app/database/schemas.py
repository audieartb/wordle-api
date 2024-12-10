from datetime import date, datetime

from pydantic import BaseModel, UUID4
from typing import Optional, List


class StatsBase(BaseModel):
    id: int
    streak: int
    solved1 = int 
    solved2 = int
    solved3 = int
    solved4 = int
    solved5 = int
    solved6 = int
    last_updated: date
    total_games = int
    user_id: UUID4
    
    class Config:
        orm_mode = True

class StatsUpdate(BaseModel):
    success: bool
    attempts: int
    user_id: UUID4
    user_email: str
    date: datetime


class UserBase(BaseModel):
    user: Optional[str] 
    email:str

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: UUID4
    stats: List[StatsBase]

    class Config:
        orm_mode = True

class Word(BaseModel):
    word: str