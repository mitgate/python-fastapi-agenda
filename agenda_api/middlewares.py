"""MIDDLEWARES
"""


from fastapi import Request


from .exceptions import *

__all__ = ("request_handler",)


async def request_handler(request: Request, call_next):
    try:
        return await call_next(request)

    except Exception as ex:
        if isinstance(ex, BaseAPIException):
            return ex.response()

        # Erro 500 
        raise ex
