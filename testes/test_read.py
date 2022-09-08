"""TESTE READ
"""

# # Installed # #
from fastapi import status as statuscode

# # Package # #
from .base import BaseTest
from .utils import *

class TestGet(BaseTest):
    def test_get_existente_pessoa(self):
        """Get Pessoa.
        Deve retornar a pessoa"""
        pessoa = get_existente_pessoa()

        response = self.get_pessoa(pessoa.pessoa_id)
        assert response.json() == pessoa.dict()

    def test_get_nonexistente_pessoa(self):
        """Get a pessoa que nao existe.
        Deve retornar 404 """
        pessoa_id = get_uuid()

        response = self.get_pessoa(pessoa_id, statuscode=statuscode.HTTP_404_NOT_FOUND)
        assert response.json()["identifier"] == pessoa_id


class TestList(BaseTest):
    def test_list_pessoas(self):
        """Lista multiplas pessoas.
        Deve retornar array"""
        pessoas = [get_existente_pessoa() for _ in range(4)]

        response = self.list_pessoas()
        assert response.json() == [p.dict() for p in pessoas]
