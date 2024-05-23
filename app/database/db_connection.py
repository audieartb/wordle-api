from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()

USER = os.getenv('DATABASE_USER')
DB_HOST = os.getenv('DB_HOST')
PWD = os.getenv('DATABASE_PWD')
POSTGRESQL_DATABASE_URL = f'postgresql://{USER}:{PWD}@{DB_HOST}/wordledb'

engine = create_engine(POSTGRESQL_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

Base.metadata.create_all(engine)


