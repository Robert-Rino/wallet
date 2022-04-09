from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

__all__ = ('users', )
from . import users
