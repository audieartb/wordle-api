from fastapi import FastAPI
from app.routers import (users, wordle)
from fastapi.middleware.cors import CORSMiddleware
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
@app.get('/')
async def root():
    return {"message":"Hello"}