# QUESTÃO 1 - Modelo SQLAlchemy/ORM

from sqlalchemy import Column, Integer, String
from .database import Base


class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    disciplina = Column(String, nullable=False)
    turma = Column(String, nullable=False)
    universidade = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    professora = Column(String, nullable=False)


class Race(Base):
    __tablename__ = "races"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    data = Column(String, nullable=True)
    local = Column(String, nullable=True)
