import json
import requests
from ..database import schemas, crud
WORD_API = "https://random-word-api.vercel.app/api?words=1&length=5"


async def get_word():
    try:
        word = requests.get(WORD_API, timeout=15)
        jsonword = json.loads(word.text)
        return jsonword[0]
    except Exception as error:
        print(error)
        return
    
async def save_game():
    try:
        pass
    except Exception as error:
        print(error)
        return
    
