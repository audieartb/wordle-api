from fastapi import FastAPI
from app.routers import users, wordle
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
app = FastAPI()

origins = [
    "http://localhost:5173"
]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
app.include_router(users.router)
app.include_router(wordle.router)
@app.get('/api/public')
async def root():
    return {"message":"Hello"}


#debugging stuff

if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0', post=8000)