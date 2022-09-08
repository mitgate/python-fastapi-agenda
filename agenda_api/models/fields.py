"""MODELS - FIELDS
"""

from pydantic import Field
from ..utils import get_time, get_uuid

__all__ = ("PessoaFields", "ContatosFields")

_string = dict(min_length=1)
_unix_ts = dict(example=get_time())


class PessoaFields:
    name = Field(
        description="Nome completo da pessoa",
        example="Leandro Rodriguez",
        **_string
    )
    contatos = Field(
        description="Contatos da pessoa"
    )
    contatos_update = Field(
        description=f"{contatos.description}. Quando atualiza substitui todos"
    )
    pessoa_id = Field(
        description="ID da pessoa na base",
        example=get_uuid(),
        min_length=36,
        max_length=36
    )
    """ pessoa_id is = _id no Mongo. Setado no PessoasRepository.create"""

    created = Field(
        alias="created",
        description="Quando a pessoa é criada ( timestamp)",
        **_unix_ts
    )
    updated = Field(
        alias="updated",
        description="Quando atualiza ( timestamp)",
        **_unix_ts
    )


class ContatosFields:
    tipo = Field(
        description="Tipo do Contato",
        example="e-mail",
        **_string
    )
    contato = Field(
        description="Dados do contato",
        example="leandro@mitgate.com.br",
        **_string
    )

