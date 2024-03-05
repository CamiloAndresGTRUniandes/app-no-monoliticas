from dataclasses import dataclass, field

from seedwork.domain.events import (DomainEvent)


@dataclass
class UserCreated(DomainEvent):
    firstName : str = field(default_factory = str)
    lastName : str = field(default_factory = str)
    userName : str = field(default_factory = str)
    password : str = field(default_factory = str)
    created_at : str = field(default_factory = str)