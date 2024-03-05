

from dataclasses import dataclass

from seedwork.domain.value_objects import ValueObject


@dataclass(frozen=True)
class Name(ValueObject):
    firstName: str
    lastName : str

