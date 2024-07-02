from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Fluffy", type="cat", id=3),
            PetsTable(name="Spot", type="dog", id=4),
        ]

def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        'data': {
            'type': 'pets',
            'count': 2,
            'attributes': [
                {"name": "Fluffy", "id": 3},
                {"name": "Spot", "id": 4},
            ],
        }
    }

    assert response == expected_response
