from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal


def get_user(email: str, hashed_password: str, db: Session=SessionLocal()):
    return db.query(models.User).filter(
        models.User.hashed_password == hashed_password,
        models.User.email == email
    ).first()


def get_user_by_email(email: str, db: Session=SessionLocal()):

    return db.query(models.User).filter(models.User.email == email).first()


def create_user(email: str, password: str, db: Session=SessionLocal()):
    # fake_hashed_password = user.password + "notreallyhashed"
    wallet = models.Wallet()
    user = models.User(
        email=email,
        hashed_password=models.User.hash_password(password),
        wallet=wallet,
    )
    db.add(wallet)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete_user(email: str, db: Session=SessionLocal()):
    if (db_user := db.query(models.User).filter(models.User.email == email).first()):
        db.delete(db_user)
        db.commit()
        return 1
    return 0


