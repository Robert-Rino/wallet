from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal


def get_user(user_id: int, db: Session=SessionLocal()):

    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(email: str, db: Session=SessionLocal()):

    return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):

#     return db.query(models.User).offset(skip).limit(limit).all()


def create_user(email: str, password: str, db: Session=SessionLocal()):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        email=email,
        hashed_password=models.User.hash_password(password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(email: str, db: Session=SessionLocal()):
    if (db_user := db.query(models.User).filter(models.User.email == email).first()):
        db.delete(db_user)
        db.commit()
        return 1
    return 0



# def get_user_items(db: Session, user_id: int, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).filter(models.Item.owner_id==user_id).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
