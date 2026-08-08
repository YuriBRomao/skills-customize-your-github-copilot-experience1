# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construir uma API REST simples com FastAPI para praticar criação de rotas, validação de dados e respostas HTTP apropriadas. Ao final, você terá um pequeno serviço web funcional para gerenciar tarefas.

## 📝 Tarefas

### 🛠️ Configurar projeto e criar primeiro endpoint

#### Descrição
Prepare o ambiente, execute a aplicação FastAPI localmente e implemente um endpoint inicial para verificar se a API está online.

#### Requisitos
O programa concluído deve:

- Instalar e usar `fastapi` e `uvicorn`
- Expor o endpoint `GET /health`
- Retornar um JSON no formato `{ "status": "ok" }`

### 🛠️ Implementar CRUD básico de tarefas

#### Descrição
Crie endpoints para listar, criar, buscar e remover tarefas usando armazenamento em memória (lista/dicionário Python).

#### Requisitos
O programa concluído deve:

- Definir um modelo `TaskCreate` com `title` e `done`
- Implementar `GET /tasks`, `POST /tasks`, `GET /tasks/{task_id}` e `DELETE /tasks/{task_id}`
- Gerar IDs inteiros sequenciais para novas tarefas

### 🛠️ Adicionar validações e respostas HTTP corretas

#### Descrição
Melhore a API com regras de validação e códigos de status apropriados para cenários de sucesso e erro.

#### Requisitos
O programa concluído deve:

- Validar que `title` não seja vazio
- Retornar `404` quando uma tarefa não existir
- Retornar `201` ao criar tarefa e `204` ao remover tarefa
