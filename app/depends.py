from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from .config import settings
from . import database, models

async def authenticate(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl='/login'))
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=['HS256'])
        if not (email := payload.get("sub")):
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    with database.SessionLocal() as session:
        if not (user := session.query(
            models.User
        ).filter(
            models.User.email == email
        ).first()):
            raise credentials_exception

    return user
