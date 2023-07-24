import requests
import json
word_api = "https://random-word-api.vercel.app/api?words=1&length=5"

async def get_word():
    
    try:
        word = requests.get(word_api)
        jsonword = json.loads(word.text)
        return jsonword[0]
    except e:
        print(e)
        return 