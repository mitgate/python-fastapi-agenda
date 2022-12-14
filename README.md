# FastAPI + MongoDB API REST - Agenda de Pessoas e seus contatos
<br/>

# Agenda de Contatos

- Exemplo de API usando FastAPI, Pydantic e configurações, Mongo database - non-async.

- O código destina-se a criar toda a documentação API com o máximo de detalhes, incluindo modelos completos e detalhados para solicitações, respostas e erros.


## END POINTS

Os endpoints definem todas as operações CRUD que podem ser realizadas nas entidades da classe Pessoa:

- GET `/docs` - Documentação OpenAPI (gerada automaticamente por FastAPI)
- GET `/pessoas` - Listar pessoas cadastradas com contatos
- GET `/pessoas/{pessoa_id}` - Ler pessoa e contatos por sua ID
- POST `/pessoas` - Criar nova pessoa e contatos
- PATCH `/pessoas/{pessoa_id}` - Atualizar pessoa e contatos
- DELETE `/pessoas/{pessoa_id}` - Excluir pessoa existente

## Estrutura do projeto (módulos)

- `app.py`: inicialização do FastAPI e de todas as rotas utilizadas pela API. Em APIs com mais endpoints e entidades diferentes, seria melhor dividir as rotas em módulos diferentes por seu contexto ou entidade.
<br />

- `models`: definição de todas as classes de modelos. Como estamos usando o MongoDB, podemos usar o mesmo esquema JSON para solicitação/resposta de API e armazenamento. Utilizando classes diferentes, dependendo do contexto:
    - `pessoa_update.py`: modelo utilizado como corpo da requisição PATCH. Inclui todos os campos de contato que podem ser atualizados.<br />
    - `pessoa_create.py`: modelo utilizado como corpo da requisição POST. Inclui todos os campos do modelo Update, mas todos os campos obrigatórios em Create devem ser declarados novamente (no tipo e no valor do campo).
    - `pessoa_read.py`: modelo utilizado como corpo de resposta GET e POST. Inclui todos os campos do modelo Create, mais o pessoa_id (que vem do campo _id no documento Mongo) .
    - `pessoa_contatos.py`: parte do modelo Pessoa, atributo contatos.
    - `common.py`: definição do BaseModel comum, do qual todas as classes do modelo herdam, direta ou indiretamente.
    - `fields.py`: definição dos Campos, que são os valores dos atributos dos modelos. Seu principal objetivo é completar a documentação do OpenAPI fornecendo uma descrição e exemplos. Os campos são declarados fora das classes devido à re-declaração necessária entre os modelos Update e Create.
    - `errors.py`: modelos de erro. Eles são referenciados nas classes Exception definidas em `exceptions.py`.
<br />    

- `database.py`: inicialização do cliente MongoDB.

- `exceptions.py`: exceções personalizadas, que podem ser traduzidas para respostas JSON que a API pode retornar (principalmente se uma Pessoa não existir ou já existir).

- `repositories.py`: métodos que interagem com a base de dados Mongo para ler ou escrever dados de Pessoa. 

- `exceptions.py`: exceções personalizadas levantadas durante o processamento da solicitação. Eles têm um modelo de erro associado, então a documentação na API pode mostrar os modelos de erro depois.

- `settings.py`: carregamento das configurações da aplicação através de variáveis de ambiente ou arquivo dotenv, usando as classes BaseSettings do Pydantic.

- `utils.py`: funções auxiliares diversas.

- `testes`: pasta com testes de aceitação e integração, executados diretamente nos endpoints da API e banco de dados Mongo real.

## Requisitos

- Python >= 3.10
- Requirements.txt[requirements.txt](requirements.txt)
- Servidor MongoDB rodando
- Docker (Opcional)


## Ferramentas no make

```bash

instalar-dependencias: ## Instalar dependencias

instalar-dependencias-teste: ## Instalar dependencias dos testes

test: ## Executar testes

run: ## Executar App

run-docker: ## Executar no docker-compose

run-docker-background: ## Executar no docker-compose, detached

remover-docker: ## Remover docker no docker-compose

iniciar-teste-mongo: ## Inicia o mongodb no docker para teste

parar-teste-mongo: ## Parar o mongodb no docker de teste

clean: ## Efetua limpeza de temporarios.
        
help: ## Exibir ajuda.

```
