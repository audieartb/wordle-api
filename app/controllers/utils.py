from ..database import schemas
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = decode_token(token)
    return user

async def decode_token(token):
    return schemas.User(id='user_id', stats=['stats'],user='name',
                        email='email@email.com')

