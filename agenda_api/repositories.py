"""REPOSITORIES
"""

# # Package # #
from .models import *
from .exceptions import *
from .database import collection
from .utils import get_time, get_uuid

__all__ = ("PessoasRepository",)


class PessoasRepository:
    @staticmethod
    def get(pessoa_id: str) -> PessoaRead:
        """Get pessoa por seu ID"""
        if document := collection.find_one({"_id": pessoa_id}):
            return PessoaRead(**document)
        else:
            raise PessoaNotFoundException(pessoa_id)

    @staticmethod
    def list() -> PessoasRead:
        """Listar pessoas """
        cursor = collection.find()
        return [PessoaRead(**document) for document in cursor]

    @staticmethod
    def create(create: PessoaCreate) -> PessoaRead:
        """Cria a pessoa e retorna objeto """
        document = create.dict()
        document["created"] = document["updated"] = get_time()
        document["_id"] = get_uuid()

        result = collection.insert_one(document)
        assert result.acknowledged

        return PessoasRepository.get(result.inserted_id)

    @staticmethod
    def update(pessoa_id: str, update: PessoaUpdate):
        """Update pessoa com campos para atualizar"""
        document = update.dict()
        document["updated"] = get_time()

        result = collection.update_one({"_id": pessoa_id}, {"$set": document})
        if not result.modified_count:
            raise PessoaNotFoundException(identifier=pessoa_id)

    @staticmethod
    def delete(pessoa_id: str):
        """Excluir pessoa com id"""
        result = collection.delete_one({"_id": pessoa_id})
        if not result.deleted_count:
            raise PessoaNotFoundException(identifier=pessoa_id)
