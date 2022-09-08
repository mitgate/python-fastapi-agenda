"""MODELS - PESSOA - UPDATE
"""

# # Native # #
from datetime import date
from typing import Optional
from contextlib import suppress

# # Package # #
from .common import BaseModel
from .fields import PessoaFields
from .pessoa_contatos import Contatos

__all__ = ("PessoaUpdate",)


class PessoaUpdate(BaseModel):
    name: Optional[str] = PessoaFields.name
    contatos:list[Contatos] | None = PessoaFields.contatos_update

