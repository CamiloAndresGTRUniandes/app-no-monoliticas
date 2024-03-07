
from dataclasses import dataclass, field

from seedwork.application.dto import DTO


@dataclass
class CompanyDTO(DTO):
    id_company: str = field(default_factory=str)
    name: str = field(default_factory=str)
    nit: str = field(default_factory=str)
    address: str = field(default_factory=str)
    city: str = field(default_factory=str)
    country: str = field(default_factory=str)