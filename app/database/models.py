from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from .db_connection import Base, POSTGRESQL_DATABASE_URL
import uuid



class User(Base):
    """Base class for game users"""
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid.uuid4)
    user = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    stats = relationship("Stats", back_populates="user")


class Stats(Base):
    """Base class for game statistics"""
    __tablename__ = 'stats'

    id = Column(Integer, primary_key=True, index=True)
    streak = Column(Integer)
    solved1 = Column(Integer)
    solved2 = Column(Integer)
    solved3 = Column(Integer)
    solved4 = Column(Integer)
    solved5 = Column(Integer)
    solved6 = Column(Integer)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    user = relationship("User", back_populates="stats")


class Words(Base):
    """Base class for words guessed in the game"""
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True, unique=True)
    word = Column(String)
    date = Column(Date)

#base = declarative_base(bind=create_async_engine(POSTGRESQL_DATABASE_URL))