import uuid

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import BOOLEAN, INTEGER, TEXT, TIMESTAMP, UUID
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    @classmethod
    def hash_password(cls, password: str):
        return password + "notreallyhashed"

    id = Column(INTEGER, primary_key=True, index=True)
    email = Column(TEXT, unique=True, index=True)
    hashed_password = Column(TEXT)
    # wallet = Column(UUID(as_uuid=True), ForeignKey('wallet.id'))
    is_active = Column(BOOLEAN, default=True)

class Wallet(Base):
    __tablename__ = 'wallet'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id = Column(INTEGER, ForeignKey('users.id'))
    amount = Column(INTEGER, default=0)

    owner = relationship(User, backref=backref('wallet', uselist=False))


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    from_user = Column(INTEGER, ForeignKey('users.id'))
    to_user = Column(INTEGER, ForeignKey('users.id'))
    amount = Column(INTEGER)
    timestamp = Column(TIMESTAMP)
