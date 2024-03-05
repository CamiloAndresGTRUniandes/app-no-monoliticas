
from dataclasses import dataclass, field

from seedwork.application.dto import DTO


@dataclass
class UserDTO(DTO):
    id_user : str = field(default_factory=str)
    firstName: str = field(default_factory=str)
    lastName: str = field(default_factory=str)
    userName: str = field(default_factory=str)
    password: str = field(default_factory=str)