"""MODELS - PESSOA - READ
"""

# # Native # #
from datetime import datetime
from typing import Optional, List

# # Installed # #
import pydantic
from dateutil.relativedelta import relativedelta

# # Package # #
from .pessoa_create import PessoaCreate
from .fields import PessoaFields

__all__ = ("PessoaRead", "PessoasRead")


class PessoaRead(PessoaCreate):
    pessoa_id: str = PessoaFields.pessoa_id
    created: int = PessoaFields.created
    updated: int = PessoaFields.updated

    @pydantic.root_validator(pre=True)
    def _set_pessoa_id(cls, data):
        """altera o campo _id para pessoa_id 
        e o a alias para "pessoa_id"  """
        if document_id := data.get("_id"):
            data["pessoa_id"] = document_id
        return data


    class Config(PessoaCreate.Config):
        extra = pydantic.Extra.ignore 


PessoasRead = List[PessoaRead]
