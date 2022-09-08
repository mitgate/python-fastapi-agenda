"""TEST WRITE
Test write actions (create, update, delete)
"""

# # Native # #
from datetime import datetime
from random import randint

# # Project # #
from agenda_api.models import *
from agenda_api.repositories import PessoasRepository

# # Installed # #
import pydantic
from freezegun import freeze_time
from dateutil.relativedelta import relativedelta
from fastapi import status as statuscode

# # Package # #
from .base import BaseTest
from .utils import *
import pprint

class PessoaAsCreate(PessoaCreate):
    """This model is used to convert PessoaRead to PessoaCreate,
     to compare the responses returned by the API with the create objects sent"""
    class Config(PessoaCreate.Config):
        extra = pydantic.Extra.ignore


class TestCreate(BaseTest):
    def test_create_pessoa(self):
        """Create a pessoa.
        Should return the pessoa"""
        create = get_pessoa_create().dict()

        response = self.create_pessoa(create)
        response_as_create = PessoaAsCreate(**response.json())
        assert response_as_create.dict() == create

    def test_timestamp_created_updated(self):
        """Create a pessoa and assert the created and updated timestamp fields.
        The creation is performed against the PessoasRepository,
        since mocking the time would not work as the testing API runs on another process"""
        iso_timestamp = "2020-01-01T00:00:00+00:00"
        expected_timestamp = int(datetime.fromisoformat(iso_timestamp).timestamp())

        with freeze_time(iso_timestamp):
            create = get_pessoa_create()
            result = PessoasRepository.create(create)

        assert result.created == result.updated
        assert result.created == expected_timestamp


class TestDelete(BaseTest):
    def test_delete_pessoa(self):
        """Delete a pessoa.
        Then get it. Should end returning 404 not found"""
        pessoa = get_existente_pessoa()

        self.delete_pessoa(pessoa.pessoa_id)
        self.get_pessoa(pessoa.pessoa_id, statuscode=statuscode.HTTP_404_NOT_FOUND)

    def test_delete_nonexistente_pessoa(self):
        """Delete a pessoa that does not exist.
        Should return not found 404 error and the identifier"""
        pessoa_id = get_uuid()

        response = self.delete_pessoa(pessoa_id, statuscode=statuscode.HTTP_404_NOT_FOUND)
        assert response.json()["identifier"] == pessoa_id


class TestUpdate(BaseTest):
    def test_update_pessoa_single_attribute(self):
        """Update the name of a pessoa.
        Then get it. Should return the pessoa with its name updated"""
        pessoa = get_existente_pessoa()

        new_name = get_uuid()
        update = PessoaUpdate(name=new_name)
        self.update_pessoa(pessoa.pessoa_id, update.dict())

        read = PessoaRead(**self.get_pessoa(pessoa.pessoa_id).json())
        assert read.name == new_name
        assert read.dict() == {**pessoa.dict(), "name": new_name, "updated": read.updated}

    def test_update_nonexistente_pessoa(self):
        """Update the name of a pessoa that does not exist.
        Should return not found 404 error and the identifier"""
        pessoa_id = get_uuid()
        update = PessoaUpdate(name=get_uuid())

        response = self.update_pessoa(pessoa_id, update.dict(), statuscode=statuscode.HTTP_404_NOT_FOUND)
        assert response.json()["identifier"] == pessoa_id

    def test_update_pessoa_none_attributes(self):
        """Update a pessoa sending an empty object.
        Should return validation error 422"""
        pessoa = get_existente_pessoa()
        self.update_pessoa(pessoa.pessoa_id, {}, statuscode=statuscode.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_update_pessoa_extra_attributes(self):
        """Update a pessoa sending unknown attributes.
        Should return validation error 422"""
        pessoa = get_existente_pessoa()
        self.update_pessoa(pessoa.pessoa_id, {"foo": "bar"}, statuscode=statuscode.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_timestamp_updated(self):
        """Update a pessoa and assert the updated timestamp.
        The update is performed against the PessoasRepository,
        since mocking the time would not work as the testing API runs on another process"""
        iso_timestamp = "2020-04-01T00:00:00+00:00"
        expected_timestamp = int(datetime.fromisoformat(iso_timestamp).timestamp())
        pessoa = get_existente_pessoa()

        with freeze_time(iso_timestamp):
            update = PessoaUpdate(name=get_uuid())
            PessoasRepository.update(pessoa_id=pessoa.pessoa_id, update=update)

        read_response = self.get_pessoa(pessoa.pessoa_id)
        read = PessoaRead(**read_response.json())

        assert read.updated == expected_timestamp
        assert read.updated != read.created
        assert read.created == pessoa.created
