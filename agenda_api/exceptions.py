"""EXCEPTIONS
"""

from typing import Type

from fastapi.responses import JSONResponse
from fastapi import status as statuscode

from .models.errors import *

__all__ = (
    "BaseAPIException",
    "BaseIdentifiedException",
    "NotFoundException", 
    "AlreadyExistsException",
    "PessoaNotFoundException",
     "PessoaAlreadyExistsException",
    "get_exception_responses"
)


class BaseAPIException(Exception):
    """Erro base da API """
    message = "Erro Geral"
    code = statuscode.HTTP_500_INTERNAL_SERVER_ERROR
    model = BaseError

    def __init__(self, **kwargs):
        kwargs.setdefault("message", self.message)
        self.message = kwargs["message"]
        self.data = self.model(**kwargs)

    def __str__(self):
        return self.message

    def response(self):
        return JSONResponse(
            content=self.data.dict(),
            status_code=self.code
        )

    @classmethod
    def response_model(cls):
        return {cls.code: {"model": cls.model}}


class BaseIdentifiedException(BaseAPIException):
    message = "Erro Interno"
    code = statuscode.HTTP_500_INTERNAL_SERVER_ERROR
    model = BaseIdentifiedError

    def __init__(self, identifier, **kwargs):
        super().__init__(identifier=identifier, **kwargs)


class NotFoundException(BaseIdentifiedException):
    message = "Nao Existe"
    code = statuscode.HTTP_404_NOT_FOUND
    model = NotFoundError


class AlreadyExistsException(BaseIdentifiedException):
    message = "Ja Existe"
    code = statuscode.HTTP_409_CONFLICT
    model = AlreadyExistsError


class PessoaNotFoundException(NotFoundException):
    message = "A pessoa nao existe"


class PessoaAlreadyExistsException(AlreadyExistsException):
    message = "A pessoa ja existe"


def get_exception_responses(*args: Type[BaseAPIException]) -> dict:
    """
    {statuscode: schema, statuscode: schema, ...}"""
    responses = dict()
    for cls in args:
        responses.update(cls.response_model())
    return responses
