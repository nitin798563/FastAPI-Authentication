from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()



DB_URL = os.getenv('DATABASE_URL')


#if you are using mySQL, then you don't need ckeck_same_thread at all. It is only for SQLite
#engine = create_engine(DB_URL, connect_args={"check_same_thread":False})

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
