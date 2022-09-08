"""TESTE - UTILS
"""

# # Native # #
from datetime import datetime
from random import randint

# # Project # #
from agenda_api.models import *
from agenda_api.repositories import PessoasRepository
from agenda_api.utils import get_uuid

__all__ = (
    "get_pessoa_create",
    "get_existente_pessoa",
    "get_uuid"
)


def get_contatos(**kwargs):
    return Contatos(**{
        "tipo": get_uuid(),
        "contato": get_uuid(),
        **kwargs
    })


def get_pessoa_create(**kwargs):
    return PessoaCreate(**{
        "name": get_uuid(),
        "contatos": [get_contatos()],
        **kwargs
    })


def get_existente_pessoa(**kwargs):
    return PessoasRepository.create(get_pessoa_create(**kwargs))
