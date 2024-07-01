from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.entities.pets import PetsTable
from .people_repository import PeopleRepository

class MockConnectionInsert:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PeopleTable)],
                    []
                )
            ]
        )

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_value, exc_traceback): pass



class MockConnectionGet:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PeopleTable)],
                    [
                        PeopleTable(first_name="João", last_name="Silva", age=30, pet_id=1)
                    ]
                )
            ]
        )

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_value, exc_traceback): pass

def test_insert_people():
    mock_connection = MockConnectionInsert()
    repo = PeopleRepository(mock_connection)
    repo.insert_person("João", "Silva", 30, 2)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()

def test_get_person():
    mock_connection = MockConnectionGet()
    repo = PeopleRepository(mock_connection)
    repo.get_person(1)

    mock_connection.session.query.assert_called_once_with(PeopleTable)
    mock_connection.session.outerjoin.assert_called_once()
    mock_connection.session.outerjoin\
        .return_value.filter.assert_called_once_with(PeopleTable.id == 1)
    mock_connection.session.outerjoin.return_value\
        .filter.return_value.with_entities.assert_called_once_with(
            PeopleTable.first_name,
            PeopleTable.last_name,
            PetsTable.name.label("pet_name"),
            PetsTable.type.label("pet_type")
        )
    mock_connection.session.outerjoin.return_value.filter\
        .return_value.with_entities.return_value.one.assert_called_once()
