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


async def getUsers():
    try:
        return[{"username":"rick"},{"username":"Morty"}]
    
    except:
        return [{"error": "error getting user"}]