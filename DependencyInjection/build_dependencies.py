from dataclasses import dataclass
from typing import Callable, cast
from Infrastructure.data.repositories import user

from Domain.users.Protocols.protocol_user import ProtocolUser

@dataclass(frozen=True)
class Dependencies:
    user: ProtocolUser

def _build_dependencies() -> Callable[[], Dependencies]:
    generate_dependencies = Dependencies(
        user=cast(ProtocolUser, user)
    )
    
    def dependencies() -> Dependencies:
        return generate_dependencies
    return dependencies

get_dependencies = _build_dependencies()