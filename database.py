from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='config.env')

database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise ValueError("A variável DATABASE_URL não está definida no ambiente!")

engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()