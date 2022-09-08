"""APP
FastAPI app inicializações e rotas
"""


import uvicorn
from fastapi import FastAPI
from fastapi import status as statuscode


from .models import *
from .exceptions import *
from .repositories import PessoasRepository
from .middlewares import request_handler
from .settings import api_settings as settings

__all__ = ("app", "run")


app = FastAPI(
    title=settings.title
)
app.middleware("http")(request_handler)


@app.get(
    "/pessoas",
    response_model=PessoasRead,
    description="Listar todas as pessoas cadastradas",
    tags=["pessoas"]
)
def _list_pessoas():
    return PessoasRepository.list()


@app.get(
    "/pessoas/{pessoa_id}",
    response_model=PessoaRead,
    description="Get pessoa com ID",
    responses=get_exception_responses(PessoaNotFoundException),
    tags=["pessoas"]
)
def _get_pessoa(pessoa_id: str):
    return PessoasRepository.get(pessoa_id)


@app.post(
    "/pessoas",
    description="Criar nova pessoa",
    response_model=PessoaRead,
    status_code=statuscode.HTTP_201_CREATED,
    responses=get_exception_responses(PessoaAlreadyExistsException),
    tags=["pessoas"]
)
def _create_pessoa(create: PessoaCreate):
    return PessoasRepository.create(create)


@app.patch(
    "/pessoas/{pessoa_id}",
    description="Atualizar pessoa utilizando ID, bem como seus dados e contatos",
    status_code=statuscode.HTTP_204_NO_CONTENT,
    responses=get_exception_responses(PessoaNotFoundException, PessoaAlreadyExistsException),
    tags=["pessoas"]
)
def _update_pessoa(pessoa_id: str, update: PessoaUpdate):
    PessoasRepository.update(pessoa_id, update)


@app.delete(
    "/pessoas/{pessoa_id}",
    description="Excluir pessoa com seu ID",
    status_code=statuscode.HTTP_204_NO_CONTENT,
    responses=get_exception_responses(PessoaNotFoundException),
    tags=["pessoas"]
)
def _delete_pessoa(pessoa_id: str):
    PessoasRepository.delete(pessoa_id)


def run():
    """Executar API com Uvicorn"""
    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port,
        log_level=settings.log_level.lower()
    )
