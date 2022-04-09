import datetime

from fastapi import APIRouter, Depends, HTTPException, Response, status, Form
from jose import jwt
from pydantic import BaseModel

from .. import schemas, crud, models, depends
from ..config import settings

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

@router.get("/user_p", status_code=200)
def protected_user(
    user = Depends(depends.get_current_user),
):
    return {
        'email': user.email
    }

# @router.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100):
#     users = crud.get_users(skip=skip, limit=limit)
#     return users


# @router.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int):
#     db_user = crud.get_user(user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


@router.post('/login')
def login(
    response: Response,
    username: str=Form(None),
    password: str=Form(None),
):
    password = password
    email = username

    hashed_password = models.User.hash_password(password)
    if (user := crud.get_user(
        email=email,
        hashed_password=hashed_password,
    )):
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
    
    response.status_code = 401
    return 
