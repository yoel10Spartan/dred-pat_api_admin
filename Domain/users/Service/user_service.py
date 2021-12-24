from typing import Any, Optional
from Domain.users.Model.user_entities import UserModel

from Domain.users.Protocols.protocol_user import ProtocolUser

def get_users(protocol: ProtocolUser) -> Optional[Any]:
    return protocol.get_all_users().all()

def delete_user(protocol: ProtocolUser, id: int) -> Optional[Any]:
    return protocol.delete_user(id)

def add_user(protocol: ProtocolUser, data: UserModel) -> Optional[Any]:
    return protocol.add_new_user(data)

def get_user(protocol: ProtocolUser, email: str) -> Optional[Any]:
    return protocol.get_an_user(email).first()