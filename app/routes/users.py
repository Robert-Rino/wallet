from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Body, Response, status

from .. import schemas, crud

router = APIRouter()

@router.post("/users/", status_code=201)
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


@router.delete("/users/")
def create_user(
    email: str,
    response: Response,
    status_code=200,
):
    # TODO: Need auth.
    if not crud.delete_user(email):
        response.status_code = status.HTTP_404_NOT_FOUND
    return 

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
