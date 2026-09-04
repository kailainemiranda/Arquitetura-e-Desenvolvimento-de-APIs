# QUESTÃO 1
# Trecho do código da classe models.py

from sqlalchemy import Column, Integer, String
from database import Base


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
