from sqlalchemy.orm import Session
from . import models, schemas


def get_user(db: Session, user_id: str):
    return db.query(models.Users).filter(models.Users.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    
    try:
        print("on crud")
        generated_id = "querty"
        new_hashed_password = user.password
        db_user = models.User(id = generated_id,user = user.user, email = user.email, hashed_password = new_hashed_password)
        db.add(db_user)
        db.commit()
        print("user added")
        db.refresh(db_user)
        return db_user
    except Exception as e:
        print("error creating user on crud ",e)
        return {"error": "error creating user","user":db_user}

def createStats(db:Session, stats: schemas.Stats,user_id : str):

    db_stats = models.Stats(**stats.dict(), user_id = user_id)
    db.add(db_stats)
    db.commit()
    db.refresh(db_stats)
    return db_stats