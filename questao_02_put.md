# QUESTÃO 2 — Método PUT

O método PUT é utilizado para atualizar os dados de uma corrida específica na API. O decorator `@app.put()` define a rota e informa que ela utiliza o método HTTP PUT.

A função assíncrona recebe o identificador da corrida pela URL, os novos dados pelo corpo da requisição e uma sessão do banco de dados. O schema é responsável pela validação dos dados recebidos antes da atualização.

A sessão do banco é utilizada para localizar a corrida pelo ID. Se o registro não existir, a API retorna HTTP 404. Se existir, os campos são atualizados, `commit()` confirma a alteração no banco e `refresh()` atualiza o objeto com os dados persistidos.

Trecho principal:

```python
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
```
