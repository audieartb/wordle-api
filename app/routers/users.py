from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
from ..controllers import users as userController
router = APIRouter()
from ..database.db_connection import SessionLocal
from ..database import models, schemas, crud
from sqlalchemy.orm import Session
from typing import List
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/api/users", tags=['users'], response_model=List[schemas.User])
async def get_users(db: Session = Depends(get_db)):
  try:
    users = await userController.get_users(db=db)
    return users
  except Exception as e:
    print(e)
    raise HTTPException(status_code=500, detail=e)


@router.get("/api/users/{user_id}", tags=['users'], response_model=schemas.User)
async def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
  user = await userController.get_user_by_id(user_id=user_id, db = db )
  return user


@router.post("/api/users", response_model=schemas.User, tags=['users'])
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
  response = await userController.createUser(user = user, db=db )
  return response.user

@router.get("/api/private")
async def token_test(token: Annotated[str, Depends(oauth2_scheme)]):
  return {"token":token}