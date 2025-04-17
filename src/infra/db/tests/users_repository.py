from src.domain.models.users import Users


class UsersRepositorySpy:

    def __init__(self):
        self.inser_user_attributes = {}
        self.select_user_attributes = {}


    def insert_user(self, first_name:str, last_name: str, age:int ) -> None:
        self.inser_user_attributes["first_name"] = first_name
        self.inser_user_attributes["last_name"] = last_name
        self.inser_user_attributes["age"] = age
        return

    def select_user(self, first_name: str) -> list[Users]:
        self.select_user_attributes["first_name"] = first_name
        return [
            Users(id=14, first_name= first_name, last_name= "test", age=14 ),
            Users(id=15, first_name= first_name, last_name= "test02", age=1402 )

        ]
