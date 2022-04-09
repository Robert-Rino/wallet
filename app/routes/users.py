import datetime

from fastapi import APIRouter, Depends, HTTPException, Response, status, Form
from jose import jwt
from pydantic import BaseModel

from .. import schemas, crud, models, depends
from ..config import settings
from app import exceptions

router = APIRouter()

class LoginInfo(BaseModel):
    email: str
    password: str

@router.post("/user", status_code=201)
def create_user(
    email: str, password: str,
):
    db_user = crud.get_user_by_email(email=email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = crud.create_user(email=email, password=password)
    
    return {
        'email': user.email,
    }


@router.delete("/user")
def create_user(
    email: str,
    response: Response,
    status_code=200,
):
    # TODO: Need auth.
    if not crud.delete_user(email):
        response.status_code = status.HTTP_404_NOT_FOUND
    return 

@router.get("/me", status_code=200)
def protected_user(
    user = Depends(depends.authenticate),
):
    return {
        'email': user.email
    }


@router.post('/login')
async def login(
    response: Response,
    username: str=Form(None),
    password: str=Form(None),
):
    password = password
    email = username

    hashed_password = models.User.hash_password(password)
    if not (user := crud.get_user(
        email=email,
        hashed_password=hashed_password,
    )):
        raise exceptions.Unauthorized()

    now = datetime.datetime.utcnow()
    response.status_code = 200
    token = jwt.encode(
        {
            'sub': user.email,
            'exp': now + datetime.timedelta(hours=1)
        }, 
        settings.secret_key, 
        algorithm='HS256',
    )
    return {
        'access_token': token,
        'token_type': 'bearer'
    }
