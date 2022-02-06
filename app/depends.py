from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from . import crud

SECRET_KEY = 'secret'

async def get_current_user(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl='/login'))
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        if not (email := payload.get("sub")):
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    if not (user := crud.get_user_by_email(email=email)):
        raise credentials_exception
    return user
