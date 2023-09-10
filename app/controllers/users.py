from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends

from ..database import models, schemas, crud




async def createUser(user: schemas.UserCreate, db: Session):
    try:
        print("on controller")
        response_model = crud.create_user(db=db,user=user)
        print(user)
        return response_model
    except Exception as e:
        print(e)
        return [{"error": "error creating user"}]        

async def get_users(db: Session):
    try:
        response_model = crud.get_users(db=db)
        return response_model
    except Exception as e:
        print(e)
        return e

async def get_user_by_id(user_id: str, db:Session):
    try:
        response_model = crud.get_user(db=db, user_id=user_id)
        return response_model
    except:
        return [{"error": "error getting user"}]