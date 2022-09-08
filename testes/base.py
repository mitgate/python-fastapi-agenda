"""TESTE - BASE
"""

# # Native # #
from multiprocessing import Process

# # Instalado # #
import httpx
from wait4it import wait_for, get_free_port

# # Projeto # #
from agenda_api import run
from agenda_api.database import collection
from agenda_api.settings import api_settings

__all__ = ("BaseTest",)


class BaseTest:
    api_process: Process
    api_url: str

    @classmethod
    def setup_class(cls):
        api_port = api_settings.port = get_free_port()
        cls.api_url = f"http://localhost:{api_port}"
        cls.api_process = Process(target=run, daemon=True)
        cls.api_process.start()
        wait_for(port=api_port)

    @classmethod
    def teardown_class(cls):
        cls.api_process.terminate()

    @classmethod
    def teardown_method(cls):
        collection.delete_many({})

    # # API  # #
    def get_pessoa(self, pessoa_id: str, statuscode: int = 200):
        r = httpx.get(f"{self.api_url}/pessoas/{pessoa_id}")
        assert r.status_code == statuscode, r.text
        return r

    def list_pessoas(self, statuscode: int = 200):
        r = httpx.get(f"{self.api_url}/pessoas")
        assert r.status_code == statuscode, r.text
        return r

    def create_pessoa(self, create: dict, statuscode: int = 201):
        r = httpx.post(f"{self.api_url}/pessoas", json=create)
        assert r.status_code == statuscode, r.text
        return r

    def update_pessoa(self, pessoa_id: str, update: dict, statuscode: int = 204):
        r = httpx.patch(f"{self.api_url}/pessoas/{pessoa_id}", json=update)
        assert r.status_code == statuscode, r.text
        return r

    def delete_pessoa(self, pessoa_id: str, statuscode: int = 204):
        r = httpx.delete(f"{self.api_url}/pessoas/{pessoa_id}")
        assert r.status_code == statuscode, r.text
        return r
