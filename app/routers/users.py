from typing import List
from sqlalchemy.orm import Session
from ..database.db_connection import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated
from ..database import schemas
from ..controllers import users as userController
from ..controllers import utils
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()


def get_db():
    """gets database connection"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#not really necessary
@router.get("/api/users", tags=['users'], response_model=List[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    """gets all users in database"""
    try:
        users = await userController.get_users(db=db)
        return users
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail=error)


#what is the purpose of this, get user statistics?, goes to get user by email/id
@router.get("/api/users/{user_id}", tags=['users'], response_model=schemas.User)
async def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
    """return user matching the id"""
    user = await userController.get_user_by_id(user_id=user_id, db=db)
    return user

#change to sign up?, should go to controller > create user
@router.post("/api/users", response_model=schemas.User, tags=['users'])
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """creates a new user"""
    user_exists = await userController.get_user_by_email(email=user.email, db=db)
    if user_exists:
        raise HTTPException(status_code=400, detail='email already registered')
    response = await userController.create_user(user=user, db=db)
    return response


#will work as log in
@router.get("/api/private")
async def token_test(token: Annotated[str, Depends(oauth2_scheme)]):
    """test for token authenticated url"""
    return {"token": token}

@router.get("/user/save")
async def save_game(stats: schemas.Stats, db: Session = Depends(get_db)):
    user_exists = await userController.get_user_by_id(email=stats.id)
    if user_exists:
        userController.save_game(stats=stats)
    return True