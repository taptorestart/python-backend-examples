from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection
username = 'root'
password = 'lo[rdb]-3216'
host = 'localhost'
port = 3306
database = 'fastapi'

SQLALCHEMY_DATABASE_URL = f'mysql://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
