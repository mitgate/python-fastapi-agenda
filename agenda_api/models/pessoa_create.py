"""MODELS - PESSOA - CREATE
Pessoa herdada de PessoaUpdate, mas os campso precisam ser redefinidos
"""

from .pessoa_update import PessoaUpdate
from .pessoa_contatos import Contatos
from .fields import PessoaFields

__all__ = ("PessoaCreate",)


class PessoaCreate(PessoaUpdate):
    name: str = PessoaFields.name
    contatos: list[Contatos] = PessoaFields.contatos

