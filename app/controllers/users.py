from sqlalchemy.orm import Session
from ..database import schemas, crud


async def create_user(user: schemas.UserCreate, db: Session):
    """creates user in db"""
    try:
        print("on controller")
        response_model = crud.create_user(db=db, user=user)
        print(user)
        return response_model
    except Exception as error:
        print(error)
        return [{"error": "error creating user"}]


async def get_users(db: Session):
    """gets all users in db"""
    try:
        response_model = crud.get_users(db=db)
        return response_model
    except Exception as error:
        print(error)
        return error

async def get_user_by_email(email:str, db: Session):
    """finds user matching email"""
    try:
        user = crud.get_user_by_email(db=db, email=email)
        return user
    except Exception as error:
        return error
async def get_user_by_id(user_id: str, db: Session):
    """gets user matching id"""
    try:
        response_model = crud.get_user(db=db, user_id=user_id)
        return response_model
    except Exception as error:
        return [{"error": "error getting user"+error}]
