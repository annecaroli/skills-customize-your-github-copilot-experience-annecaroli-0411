# 📘 Assignment: Persistência de Dados em APIs FastAPI

## 🎯 Objective

Aprimore uma API FastAPI substituindo o armazenamento em memória por um banco SQLite acessado com SQLAlchemy. Ao final, os dados do catálogo continuarão disponíveis mesmo depois que a API for reiniciada.

## 📝 Tasks

### 🛠️ Modelar os Dados e Configurar o Banco

#### Descrição
Use o código inicial para definir o modelo SQLAlchemy dos itens e configurar a conexão com um banco SQLite local.

#### Requisitos
O programa concluído deve:

- Instalar FastAPI, Uvicorn e SQLAlchemy com `python -m pip install fastapi uvicorn sqlalchemy`.
- Mapear os campos `id`, `name`, `price` e `in_stock` em uma tabela `items`.
- Criar as tabelas necessárias ao iniciar a aplicação.
- Fornecer uma sessão do banco por requisição e fechá-la ao final.

### 🛠️ Persistir a Criação e a Consulta de Itens

#### Descrição
Conecte as rotas de listagem, consulta por identificador e criação ao banco de dados, removendo a dependência da lista em memória.

#### Requisitos
O programa concluído deve:

- Usar consultas SQLAlchemy para listar os itens e buscar um item pelo identificador.
- Salvar novos itens no banco e confirmar a transação.
- Retornar status `404` quando o identificador consultado não existir.
- Retornar os dados do item criado, incluindo o identificador gerado pelo banco.

### 🛠️ Atualizar e Remover Dados Persistidos

#### Descrição
Adapte as rotas de atualização e remoção para operar sobre os registros do SQLite e verifique que as alterações sobrevivem à reinicialização da API.

#### Requisitos
O programa concluído deve:

- Atualizar os campos de um item existente e salvar a transação.
- Remover um item existente e confirmar a transação.
- Retornar status `404` quando uma atualização ou remoção solicitar um item inexistente.
- Reiniciar a API e confirmar que os itens criados continuam armazenados.