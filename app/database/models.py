from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .db_connection import Base, engine

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    user = Column(String)
    email = Column(String, unique=True,index=True)
    hashed_password = Column(String)

    stats = relationship("Stats", back_populates="user")
    
class Stats(Base):
    __tablename__ = 'stats'

    id = Column(Integer, primary_key=True, index=True)
    streak = Column(Integer)
    solved1 = Column(Integer) 
    solved2 = Column(Integer)
    solved3 = Column(Integer)
    solved4 = Column(Integer)
    solved5 = Column(Integer)
    solved6 = Column(Integer)
    user_id = Column(String, ForeignKey("users.id"))

    user = relationship("User", back_populates="stats")

class Words(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True,unique=True)
    word = Column(String)
    date = Column(Date)

Base.metadata.create_all(engine)