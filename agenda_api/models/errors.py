"""MODELS - ERRO
"""

# # Installed # #
from pydantic import BaseModel, Field

__all__ = ("BaseError", "BaseIdentifiedError", "NotFoundError", "AlreadyExistsError")


class BaseError(BaseModel):
    message: str = Field(..., description="Mensagem de Erro ")


class BaseIdentifiedError(BaseError):
    identifier: str = Field(..., description="ID do Erro")


class NotFoundError(BaseIdentifiedError):
    pass


class AlreadyExistsError(BaseIdentifiedError):
    pass
