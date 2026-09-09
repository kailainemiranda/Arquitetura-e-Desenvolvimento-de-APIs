# 🧠 MindP2P API — Incentive-Driven Knowledge Peer Engine

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg)

Uma API RESTful desenvolvida com **FastAPI** e **SQLAlchemy** que calcula dinamicamente a taxa de retenção de conhecimento de estudantes usando a **Curva do Esquecimento de Ebbinghaus** para automatizar o pareamento P2P de monitorias.

## 🚀 Funcionalidades Principais
- **Cálculo de Retenção Dinâmico:** Aplica a fórmula $R = e^{-t/S}$ para estimar a decadência da memória em cada matéria.
- **Matchmaking Inteligente:** Conecta alunos que têm fraquezas em disciplinas onde outros possuem retenção superior a 70%.
- **Persistência de Dados:** Banco SQL via ORM SQLAlchemy.
- **Arquitetura Testável:** Suíte de testes automatizados com Pytest.

## 📦 Como Rodar o Projeto Localmente

1. Clone o repositório ou descompacte o arquivo zip:
   ```bash
   cd mindp2p-api
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Acesse a documentação interativa OpenAPI no navegador:
   `http://127.0.0.1:8000/docs`

## 🧪 Rodando os Testes
```bash
pytest
```
