from sqlalchemy.orm import sessionmaker, session, create_session, scoped_session
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')


def exist_database(db_name, engine):
    query = text(f'SHOW DATABASES LIKE "{db_name}"')
    with engine.connect() as connection:
        check = connection.execute(query)
        return check.fetchone() is not None

def create_database(db_name, engine):
    with engine.connect() as connection:
        connection.execute(text(f'CREATE DATABASE {db_name}'))
        

def get_bank_school(db_name):
    name_db = db_name
    server_engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/')
    
    
    if not exist_database(name_db, server_engine):
        create_database(name_db, server_engine)
        
    engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{db_name}')
    return engine

def get_session_for_school(school_name):
    engine = get_bank_school(school_name)
    Session = scoped_session(sessionmaker(bind=engine))
    
    return Session
