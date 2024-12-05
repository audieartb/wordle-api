from datetime import date, datetime

from pydantic import BaseModel
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
    last_updated: datetime
    total_games = int
    user_id: str
    
    class Config:
        orm_mode = True

class StatsUpdate(BaseModel):
    id: Optional[int] = None
    success: bool
    attempts: int
    user_id: int
    user_email: str
    date: datetime


class UserBase(BaseModel):
    user: str
    email:str

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: str
    stats: List[StatsBase]

    class Config:
        orm_mode = True