# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar um catálogo de itens usando FastAPI. Pratique rotas HTTP, validação de dados com modelos Pydantic e respostas com códigos de status apropriados.

## 📝 Tasks

### 🛠️ Configurar a API e Consultar Itens

#### Descrição
Use o código inicial como base para criar a aplicação FastAPI e implementar rotas para listar os itens e consultar um item pelo identificador.

#### Requisitos
O programa concluído deve:

- Instalar FastAPI e Uvicorn com `python -m pip install fastapi uvicorn`.
- Salvar o código da aplicação como `main.py` e iniciá-lo com `uvicorn main:app --reload`.
- Implementar `GET /items` para retornar todos os itens.
- Implementar `GET /items/{item_id}` para retornar um item ou responder com status `404` quando ele não existir.

### 🛠️ Criar, Atualizar e Remover Itens

#### Descrição
Implemente as operações para adicionar itens ao catálogo, substituir os dados de um item existente e removê-lo.

#### Requisitos
O programa concluído deve:

- Implementar `POST /items` para criar um item e responder com status `201`.
- Implementar `PUT /items/{item_id}` para atualizar um item existente.
- Implementar `DELETE /items/{item_id}` para remover um item e responder com status `204`.
- Responder com status `404` quando uma atualização ou remoção solicitar um identificador inexistente.

### 🛠️ Validar Dados e Testar a API

#### Descrição
Use os modelos Pydantic e a documentação interativa do FastAPI para conferir o comportamento da API com entradas válidas e inválidas.

#### Requisitos
O programa concluído deve:

- Validar que o nome do item não esteja vazio e que o preço seja maior que zero.
- Abrir `/docs` e testar cada rota com exemplos de requisição.
- Confirmar os códigos de status de sucesso e de erro descritos nas tarefas anteriores.