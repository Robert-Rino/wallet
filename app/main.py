from app.exceptions import Unauthorized
from fastapi import Request
from fastapi.responses import JSONResponse

from typing import List, Optional
# from .routes import users
from . import routes, create_app

app = create_app()
app.include_router(routes.router)
app.include_router(routes.users.router)


@app.exception_handler(Unauthorized)
async def unauthorized(request: Request, exc: Unauthorized):
    return JSONResponse(
        status_code=401,
        content={'code': exc.code},
    )


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post('/token')
# async def login(
#     form_data: OAuth2PasswordRequestForm = Depends(),
#     db: Session = Depends(get_db)
# ):
#     user = crud.get_user_by_email(db, form_data.username)
#     if not user or not (user.hashed_password == models.User.hash_password(form_data.password)):
#         raise HTTPException(status_code=400, detail='Incorrect username or password')

#     access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.email}, expires_delta=access_token_expires
#     )

#     return {"access_token": access_token, "token_type": "bearer"}


# async def get_current_user(
#         token: str = Depends(OAuth2PasswordBearer(tokenUrl="token")),
#         db: Session = Depends(get_db)
#     ):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         print(username)
#         if username is None:
#             raise credentials_exception
#         token_data = schemas.TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = crud.get_user_by_email(db, username)
#     if user is None:
#         raise credentials_exception
#     return user

# @app.get("/me", response_model=schemas.User)
# async def read_me(current_user: schemas.User = Depends(get_current_user)):
#     return current_user

# @app.post("/items", response_model=schemas.Item)
# def create_item_for_user(
#     item: schemas.ItemCreate,
#     current_user: schemas.User= Depends(get_current_user),
#     db: Session = Depends(get_db),
# ):
#     return crud.create_user_item(db=db, item=item, user_id=current_user.id)


# @app.get("/items", response_model=List[schemas.Item])
# def read_items(
#         skip: int = 0, 
#         limit: int = 100, 
#         current_user: schemas.User= Depends(get_current_user),
#         db: Session = Depends(get_db)
# ):
#     items = crud.get_user_items(db, user_id=current_user.id, skip=skip, limit=limit)
#     return items
