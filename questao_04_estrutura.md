# QUESTÃO 4 — Organização dos diretórios

A organização do projeto FastAPI separa as responsabilidades da aplicação.

## models

O diretório `models` contém os modelos do banco de dados desenvolvidos com SQLAlchemy ORM. Os modelos representam as tabelas e seus respectivos campos.

## schemas

O diretório `schemas` contém os schemas utilizados para validação e serialização dos dados. Com Pydantic, é possível definir a estrutura dos dados recebidos e retornados pela API.

## core

O diretório `core` concentra configurações e componentes essenciais utilizados pela aplicação, como a configuração do CORS.

## database

O arquivo `database.py` concentra a conexão com o banco e o gerenciamento das sessões.

## main

O arquivo `main.py` cria a aplicação FastAPI e reúne os endpoints.

Essa separação de responsabilidades deixa o projeto mais organizado, facilita a manutenção, a reutilização de componentes e a evolução da aplicação.
