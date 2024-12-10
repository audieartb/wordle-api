from typing import List
from sqlalchemy.orm import Session
from ..database.db_connection import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
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


# ALL USERS FOR ADMIN ENDPOINT - NOT IN USE
# @router.get("/api/users", tags=['users'], response_model=List[schemas.User])
# async def get_users(db: Session = Depends(get_db)):
#     """gets all users in database"""
#     try:
#         users = await userController.get_users(db=db)
#         return users
#     except Exception as error:
#         print(error)
#         raise HTTPException(status_code=500, detail=error)

# GET ONE USER BY ID
@router.get("/api/user/{user_id}", tags=['users'], response_model=schemas.User)
async def get_user_by_id(user_id: str, 
                         current_user: Annotated[schemas.UserBase, Depends(utils.get_current_user)], 
                         db: Session = Depends(get_db)):
    """return user matching the id"""
    user = await userController.get_user_by_email(user_id=user_id, db=db)
    return user


###### IMPORTANT - LOGIN#########
@router.post('/token', tags=['auth'])
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    """Log in for existing users"""
    user_dict = await userController.get_user_by_email(form_data.username, db=db)
    user = schemas.UserCreate(
        user='', email=form_data.username, password=form_data.password)
    if not user_dict:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
    login_response = await userController.login(user=user, db=db)
    return login_response


# change to sign up?, should go to controller > CREATE USER WORKS
@router.post("/api/users/signup", tags=['users'])
async def sign_up(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """creates a new user"""
    user_exists = await userController.get_user_by_email(email=user.email, db=db)
    if user_exists:
        raise HTTPException(status_code=400, detail='email already registered')
    response = await userController.create_user(user=user, db=db)
    return response


# UPDATE AFTER EVERY GAME
@router.put("/api/users", response_model=schemas.StatsBase, tags=['users'])
async def update_score(score: schemas.StatsUpdate,
                       current_user: Annotated[schemas.UserBase, Depends(utils.get_current_user)],
                       db: Session = Depends(get_db)):
    """updates the stats of an existing user"""
    user_exists = await userController.get_user_by_email(email=current_user, db=db)
    if not user_exists:
        raise HTTPException(status_code=400, detail='Invalid user')
    new_stats = await userController.update_stats(stats=score, db=db)
    return new_stats
