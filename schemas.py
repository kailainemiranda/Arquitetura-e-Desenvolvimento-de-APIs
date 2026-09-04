# QUESTÃO 2 - Schema para validação dos dados do PUT

from pydantic import BaseModel


class RaceSchema(BaseModel):
    nome: str
    data: str | None = None
    local: str | None = None


class RaceResponse(RaceSchema):
    id: int

    class Config:
        from_attributes = True
