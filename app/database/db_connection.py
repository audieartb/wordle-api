from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()

USER = os.environ['DATABASE_USER']
DB_HOST = os.environ.get('DB_HOST')
PWD = os.environ.get('DATABASE_PWD')
POSTGRESQL_DATABASE_URL = f'postgresql+psycopg2://{USER}:{PWD}@{DB_HOST}/wordledb'

engine = create_engine(POSTGRESQL_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
