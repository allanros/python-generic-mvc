import re
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface

class PersonCreatorController:
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def create(self, person_info: dict) -> dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validate_name(first_name, last_name)
        self.__validate_number(age)
        self.__validate_number(pet_id)
        self.__insert_person_in_db(first_name, last_name, age, pet_id)

        return self.__format_response(person_info)

    def __validate_name(self, first_name: str, last_name: str) -> None:
        non_valid_caracters = re.compile(r'[^a-z A-Z]')

        if non_valid_caracters.search(first_name) or non_valid_caracters.search(last_name):
            raise Exception("Invalid name")

    def __validate_number(self, number: int) -> None:
        if not isinstance(number, int) and number < 0:
            raise Exception("Invalid number")

    def __insert_person_in_db(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self.__people_repository.insert_person(first_name, last_name, age, pet_id)

    def __format_response(self, person_info: dict) -> dict:
        return {
            "data": {
                "type": "person",
                "count": 1,
                "attributes": person_info
            }
        }
