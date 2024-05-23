from pydantic import BaseModel
import uuid
class StatsBase(BaseModel):
    streak: int
    solved1 : int 
    solved2 : int
    solved3 : int
    solved4 : int
    solved5 : int
    solved6 : int

class StatsCreate(StatsBase):
    pass

class Stats(StatsBase):
    id: int
    user_id: uuid.UUID

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    user: str
    email:str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: uuid.UUID
    stats: list[Stats] = []

    class Config:
        orm_mode = True