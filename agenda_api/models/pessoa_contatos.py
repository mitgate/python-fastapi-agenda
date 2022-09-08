"""MODELS - PESSOA 
"""

from .common import BaseModel
from .fields import ContatosFields

__all__ = ("Contatos",)


class Contatos(BaseModel):
    tipo: str = ContatosFields.tipo
    contato: str = ContatosFields.contato
