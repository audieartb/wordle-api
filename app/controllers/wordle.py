import json
import requests
from sqlalchemy.orm import Session
from ..database import crud
from datetime import date
from fastapi import HTTPException

WORD_API = "https://random-word-api.vercel.app/api?words=1&length=5"

async def get_word(db: Session):
    try:
        daily_word = await crud.get_word(db=db)
        if not daily_word:
            raise HTTPException(status_code=404)
        return daily_word.word

    except Exception as error:
        return {"error getting word": error}


async def set_daily_word(db: Session):
    try:
        check_current = await crud.get_word(db=db)
        if check_current.date == date.today():
            return check_current.word
        
        word = requests.get(WORD_API, timeout=15)
        jsonword = json.loads(word.text)
        print(jsonword[0])
        await crud.save_word(word=jsonword[0], db=db)
        return jsonword[0]
    except Exception as error:
        return error
