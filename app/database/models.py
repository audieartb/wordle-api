from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid
Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    user = Column(String)
    email = Column(String, unique=True,index=True)
    hashed_password = Column(String)

    stats = relationship("Stats", back_populates="user")
    
class Stats(Base):
    __tablename__ = 'stats'

    id = Column(Integer, primary_key=True, index=True)
    streak = Column(Integer, default=0)
    solved1 = Column(Integer, default=0) 
    solved2 = Column(Integer, default=0)
    solved3 = Column(Integer, default=0)
    solved4 = Column(Integer, default=0)
    solved5 = Column(Integer, default=0)
    solved6 = Column(Integer, default=0)
    last_updated = Column(Date)
    total_games = Column(Integer, default=0)
    user_id = Column(UUID, ForeignKey("users.id"))

    user = relationship("User", back_populates="stats")

class Words(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True,unique=True)
    word = Column(String)
    date = Column(Date)