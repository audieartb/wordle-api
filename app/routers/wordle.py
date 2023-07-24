from fastapi import APIRouter

from ..controllers import wordle as wordleController

router = APIRouter()

@router.get("/getword", tags=["getword"])
async def get_word():
    
    word = await wordleController.get_word()
    return word

