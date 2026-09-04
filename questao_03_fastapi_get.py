# QUESTÃO 3
# Configuração da FastAPI e criação da rota GET

from fastapi import FastAPI

app = FastAPI(
    title="Bem vindo à disciplina Arquitetura e Desenvolvimento de APIs",
    version="1.0.0",
    description="KAILAINE BARBOSA MIRANDA - RU 4832461"
)


@app.get("/races")
def get_races():
    return {
        "message": "Consulta de corridas realizada com sucesso"
    }
