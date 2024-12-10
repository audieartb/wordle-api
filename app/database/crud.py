from sqlalchemy.orm import Session
from . import models, schemas
import uuid
from datetime import datetime

def generate_uid():
    return uuid.uuid4()

def get_user(db: Session, user_id: str):
    """finds user matching user_id"""
    try:
        user =  db.query(models.User).filter(models.User.id == user_id).first()
        return user
    except Exception as error:
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

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    """creates user in db, assigns uid and hashes password"""
    try:
        db_user = models.User(user = user.user, email = user.email, hashed_password = hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as error:
        return {"error": "error creating user","user":db_user}

def create_stats(db:Session,user_id : str):
    """creates game stats from user_id"""
    #db_stats = models.Stats(**stats.dict(), user_id = user_id)
    try:
        
        db_stats = models.Stats(user_id = user_id, last_updated=datetime.now())
        db.add(db_stats)
        db.commit()
        db.refresh(db_stats)
        return db_stats
    except Exception as error:
        return {"Error Creating Stats":error}
    
def update_stats(db:Session, stats: schemas.StatsUpdate):
    """update the user stats"""
    try:

        db_stats = db.query(models.Stats).filter(models.Stats.user_id == stats.user_id).first()
        db_stats.last_updated = datetime.now()
        db_stats.total_games += 1
        if not stats.success:
            db_stats.streak = 0
            db.add(db_stats)
        else:
            db_stats.streak += 1
            db_stats.total_games +=1
            attribute_name = f'solved{stats.attempts}'
            current_value = getattr(db_stats, attribute_name)
            setattr(db_stats,attribute_name, current_value + 1)
            db.add(db_stats)
        db.commit()
        db.refresh(db_stats)
        return db_stats
    
    except Exception as error:
        return {"Error Updating Stats in CRUD":error}

def get_stats(db: Session, id: str):
    db_stats =  db.query(models.Stats).filter(models.Stats.user_id == id).first()
    return db_stats