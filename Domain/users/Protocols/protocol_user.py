from typing import Protocol

from Domain.users.Model.user_entities import UserModel

class ProtocolUser(Protocol):
    def get_all_users(self):
        ...

    def delete_user(self, id: int):
        ...
    
    def add_new_user(self, data: UserModel):
        ...

    def get_an_user(self, email: str):
        ...