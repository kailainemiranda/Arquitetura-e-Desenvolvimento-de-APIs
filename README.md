# Arquitetura e Desenvolvimento de APIs

**Aluno:** KAILAINE BARBOSA MIRANDA  
**RU:** 4832461  
**Disciplina:** Arquitetura e Desenvolvimento de APIs

Projeto organizado de acordo com as **Questões 1 a 6** da atividade, mantendo a numeração correspondente ao enunciado.

## Estrutura

```text
GitHub_Arquitetura_Desenvolvimento_APIs/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── core.py
│   └── main.py
├── frontend/
│   └── RacesList.vue
├── questoes/
│   ├── questao_01_models.py
│   ├── questao_02_put.md
│   ├── questao_03_fastapi_get.py
│   ├── questao_04_estrutura.md
│   ├── questao_05_vue_axios_cors.md
│   └── questao_06_get_por_id.py
├── requirements.txt
└── README.md
```

## Questão 1 — models.py

Implementação do modelo SQLAlchemy/ORM com os campos solicitados no enunciado: `id`, `nome`, `cpf`, `disciplina`, `turma`, `universidade`, `cidade` e `professora`.

Arquivo correspondente: `questoes/questao_01_models.py` e `app/models.py`.

## Questão 2 — Método PUT

Implementação do método `PUT` para atualizar uma corrida específica. A rota recebe o `race_id`, valida os dados pelo schema, consulta a sessão do banco, atualiza o registro, executa `commit()` e `refresh()` e retorna `404` quando a corrida não existe.

Arquivo correspondente: `questoes/questao_02_put.md` e `app/main.py`.

## Questão 3 — Rota GET e configuração da FastAPI

A aplicação foi configurada com:

- `title`: Bem vindo à disciplina Arquitetura e Desenvolvimento de APIs
- `version`: 1.0.0
- `description`: nome e RU do aluno

Também foi criada a rota `GET /races`.

Arquivo correspondente: `questoes/questao_03_fastapi_get.py` e `app/main.py`.

## Questão 4 — Organização do projeto

A estrutura separa as responsabilidades:

- `models`: modelos/tabelas do banco.
- `schemas`: validação e serialização dos dados.
- `core`: configurações essenciais, incluindo CORS.
- `database`: conexão e sessão do banco.
- `main`: aplicação e endpoints.

Arquivo correspondente: `questoes/questao_04_estrutura.md`.

## Questão 5 — Vue.js, Axios, v-for e CORS

O componente `RacesList.vue` utiliza Axios para consumir a API, a função assíncrona `fetchRaces()` para buscar os dados e `v-for` para percorrer e exibir a lista de corridas. O FastAPI utiliza CORS para permitir a comunicação entre origens diferentes.

Arquivo correspondente: `frontend/RacesList.vue` e `questoes/questao_05_vue_axios_cors.md`.

## Questão 6 — GET /races/{race_id}

Implementação do endpoint `GET /races/{race_id}`. Quando o ID existe, a corrida é retornada. Quando não existe, a API retorna HTTP `404`.

Arquivo correspondente: `questoes/questao_06_get_por_id.py` e `app/main.py`.

## Execução

Instalar as dependências:

```bash
pip install -r requirements.txt
```

Executar:

```bash
uvicorn app.main:app --reload
```

Documentação automática:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

- `GET /races`
- `GET /races/{race_id}`
- `PUT /races/{race_id}`
