import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

# db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="interação com o banco")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print("\n", response)

@pytest.mark.skip(reason="interação com o banco")
def test_delete_pet():
    repo = PetsRepository(db_connection_handler)
    repo.delete_pets("belinha")

@pytest.mark.skip(reason="interação com o banco")
def test_insert_people():
    repo = PeopleRepository(db_connection_handler)
    repo.insert_person("João", "Silva", 30, 2)
