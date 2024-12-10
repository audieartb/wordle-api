from ..database import schemas
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import timedelta, datetime, timezone
import jwt
from jwt.exceptions import InvalidTokenError


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


SECRET_KEY = "5bf41d57c43990c99f5542098f9bca6765b116717234e65aaf6170ef91abfd87"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MIN = 120

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Token(BaseModel):
    access_token: str
    token_type: str

def verify_password(plain_password : str, hashed_password: str):
    return pwd_context.verify(plain_password,hashed_password)

def hash_password(password: str):
    return pwd_context.hash(password)

def authenticate(username: str, password: str):
    db_password = 'string'
    if not verify_password(plain_password=password, hashed_password=db_password):
        return False
    return True

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc)+expires_delta
    else:
        expire = datetime.now(timezone.utc)+timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



async def decode_token(token):
    return  token


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try: 
        payload = jwt.decode(token,SECRET_KEY, algorithms=ALGORITHM)
        username : str = payload.get("sub")
        return username
    except InvalidTokenError:
        raise credentials_exception