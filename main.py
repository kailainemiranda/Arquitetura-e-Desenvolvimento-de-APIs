# QUESTÕES 2, 3 e 6 - Endpoints da API

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .core import configure_cors
from .database import Base, engine, get_db
from .models import Race
from .schemas import RaceResponse, RaceSchema

Base.metadata.create_all(bind=engine)

# QUESTÃO 3 - Configuração da aplicação FastAPI
app = FastAPI(
    title="Bem vindo à disciplina Arquitetura e Desenvolvimento de APIs",
    version="1.0.0",
    description="KAILAINE BARBOSA MIRANDA - RU 4832461"
)

configure_cors(app)


# QUESTÃO 3 - Endpoint GET para consulta de corridas
@app.get("/races", response_model=list[RaceResponse])
def get_races(db: Session = Depends(get_db)):
    return db.query(Race).all()


# QUESTÃO 6 - GET /races/{race_id} com retorno 404
@app.get("/races/{race_id}", response_model=RaceResponse)
def get_race(race_id: int, db: Session = Depends(get_db)):
    race = db.query(Race).filter(Race.id == race_id).first()

    if race is None:
        raise HTTPException(
            status_code=404,
            detail="Corrida não encontrada"
        )

    return race


# QUESTÃO 2 - PUT para atualização de uma corrida específica
@app.put("/races/{race_id}", response_model=RaceResponse)
async def update_race(
    race_id: int,
    race: RaceSchema,
    db: Session = Depends(get_db)
):
    db_race = db.query(Race).filter(Race.id == race_id).first()

    if db_race is None:
        raise HTTPException(
            status_code=404,
            detail="Corrida não encontrada"
        )

    db_race.nome = race.nome
    db_race.data = race.data
    db_race.local = race.local

    db.commit()
    db.refresh(db_race)

    return db_race
