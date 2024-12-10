from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..database import schemas, crud
from . import utils
from datetime import datetime, timedelta
import json

# for signing up


async def create_user(user: schemas.UserCreate, db: Session):
    """creates user in db"""
    try:
        hashed_password = utils.hash_password(user.password)
        response_model = crud.create_user(
            db=db, user=user, hashed_password=hashed_password)
        crud.create_stats(db=db, user_id=response_model.id)
        expire_delta = timedelta(minutes=120)
        token = utils.create_access_token(
            data={"sub": user.email}, expires_delta=expire_delta)
        return token
    except Exception as error:
        print(error)
        return [{"Sign-up Error": error}]


async def login(user: schemas.UserCreate, db: Session):
    try:
        user_db = crud.get_user_by_email(db=db, email=user.email)
        if not utils.verify_password(plain_password=user.password, hashed_password=user_db.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Invalid Credentials", headers={"WWW-Authenticate": "Bearer"})
        token = utils.create_access_token(
            data={"sub": user_db.email}, expires_delta=timedelta(minutes=120))
        return {"access_token": token, "token_type": "bearer"}

    except Exception as error:
        return [{"Login Error": error}]

# should not be used


async def get_users(db: Session):
    """gets all users in db"""
    try:
        response_model = crud.get_users(db=db)
        return response_model
    except Exception as error:
        print(error)
        return error

# shoudl return user data and statistics


async def get_user_by_email(email: str, db: Session):
    """finds user matching email"""
    try:
        user = crud.get_user_by_email(db=db, email=email)
        return user
    except Exception as error:
        return error

# probably delete it and leave get user by email


async def get_user_by_id(user_id: str, db: Session):
    """gets user matching id"""
    try:
        response_model = crud.get_user(db=db, user_id=user_id)
        return response_model
    except Exception as error:
        return [{"error": "error getting user"+error}]


# checks last updated to check streak
# updates last_udpated and solve in number
# resets streak if difference in days is more than 1
async def update_stats(stats: schemas.StatsUpdate, db: Session):
    try:
        print("in controller")
        # get stored stats if any
        db_stats = crud.update_stats(stats=stats, db=db)
        if not db_stats:
            print("no stats for this user")
            return
        # checks last updated to check streak
        return db_stats
    except Exception as error:
        return [{"error": "error getting user"+error}]
    pass
