from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import wordle as wordleController
from ..database.db_connection import SessionLocal

router = APIRouter()

def get_db():
    """gets database connection"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/getword", tags=["getword"])
async def get_word(db: Session = Depends(get_db)):
    word = await wordleController.get_word(db=db)
    return word

@router.post('/api/word', status_code=200)
async def set_word(db: Session=Depends(get_db)):
    word = await wordleController.set_daily_word(db=db)
    return {'status': word}