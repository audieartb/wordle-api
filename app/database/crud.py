from sqlalchemy.orm import Session
from . import models, schemas
import uuid

def generate_uid():
    return uuid.uuid4()

def get_user(db: Session, user_id: str):
    """finds user matching user_id"""
    try:
        user =  db.query(models.User).filter(models.User.id == user_id).first()
        return user
    except Exception as error:
        print(error)
        return {"error":error}
    
def get_user_by_email(db: Session, email: str):
    """finds user by email"""
    try:
        user = db.query(models.User).filter(models.User.email == email).first()
        return user
    except Exception as error:
        return error

def get_users(db:Session):
    """finds and returns all users"""
    try:
        users = db.query(models.User).all()
        return users
    except Exception as error:
        return error

def create_user(db: Session, user: schemas.UserCreate):
    """creates user in db, assigns uid and hashes password"""
    try:
        print("on crud")
        generated_id = generate_uid()
        new_hashed_password = user.password
        db_user = models.User(id = generated_id,user = user.user, email = user.email, hashed_password = new_hashed_password)
        db.add(db_user)
        db.commit()
        print("user added")
        db.refresh(db_user)
        return db_user
    except Exception as error:
        print("error creating user on crud ",error)
        return {"error": "error creating user","user":db_user}

def create_stats(db:Session, stats: schemas.Stats,user_id : str):
    """creates game stats from user_id"""
    db_stats = models.Stats(**stats.dict(), user_id = user_id)
    db.add(db_stats)
    db.commit()
    db.refresh(db_stats)
    return db_stats