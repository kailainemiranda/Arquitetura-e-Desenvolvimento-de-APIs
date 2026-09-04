# QUESTÃO 6
# GET /races/{race_id} com retorno 404 caso o ID não exista

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Race

app = FastAPI()


@app.get("/races/{race_id}")
def get_race(race_id: int, db: Session = Depends(get_db)):
    race = db.query(Race).filter(Race.id == race_id).first()

    if race is None:
        raise HTTPException(
            status_code=404,
            detail="Corrida não encontrada"
        )

    return race
