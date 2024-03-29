
from dataclasses import dataclass, field

from seedwork.application.dto import DTO


@dataclass
class SalesDTO(DTO):
    id_property : str = field(default_factory=str)
    name: str = field(default_factory=str)
    price: str = field(default_factory=str)
    currency: str = field(default_factory=str)
    property_id : str = field(default_factory=str)