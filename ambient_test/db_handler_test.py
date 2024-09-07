from sqlalchemy.orm import sessionmaker, session, create_session, scoped_session, declarative_base
from sqlalchemy import create_engine, text, Column, Integer, String, DateTime, ForeignKey, Text
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

Base = declarative_base()

class Matricula(Base):
    
    __tablename__ = 'Matrículas'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    aluno_id = Column(Integer, nullable=False, autoincrement=True)
    data_matricula = Column(DateTime, default=datetime.datetime.utcnow)
    ano_letivo = Column(Integer, nullable=False)
    status = Column(String(20), default='ativa')  # ativa, trancada, cancelada, concluída
    periodo_letivo = Column(String(20), nullable=True)  # ex: 1º semestre
    modalidade = Column(String(50), nullable=False)  # presencial, EAD, híbrido
    data_cancelamento = Column(DateTime, nullable=True)
    notas_finais = Column(Text, nullable=True)  # pode ser usado JSON para mais flexibilidade
    forma_pagamento = Column(String(50), nullable=True)
    observacoes = Column(Text, nullable=True)
    
    def __repr__(self):
        return f"<Matricula(id={self.id}, aluno_id={self.aluno_id}, curso_id={self.curso_id}, status={self.status})>"

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
    
    Base.metadata.create_all(engine)
    
    return engine

def get_session_for_school(school_name):
    engine = get_bank_school(school_name)
    Session = scoped_session(sessionmaker(bind=engine))
    
    return Session


get_session_for_school('test')
