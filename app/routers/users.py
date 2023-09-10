from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
from ..controllers import users as userController
router = APIRouter()
from ..database.db_connection import SessionLocal
from ..database import models, schemas, crud
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/api/users", tags=['users'])
async def get_users():
  user = await userController.getUsers()
  return user

@router.post("/api/users", response_model=schemas.User, tags=['users'])
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
  response = await userController.createUser(user = user, db=db )
  return response.user

@router.get("/api/private")
async def token_test(token: Annotated[str, Depends(oauth2_scheme)]):
  return {"token":token}