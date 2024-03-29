from dataclasses import dataclass, field

from seedwork.domain.events import (DomainEvent)


@dataclass
class CompanyCreated(DomainEvent):
    id: str = field(default_factory=str)
    name: str = field(default_factory=str)
    nit: str = field(default_factory=str)
    address: str = field(default_factory=str)
    city: str = field(default_factory=str)
    country: str = field(default_factory=str)
    property_id: str = field(default_factory=str)


@dataclass
class CompanyPropertyAssociated(DomainEvent):
    id: str = field(default_factory=str)
    name: str = field(default_factory=str)
    nit: str = field(default_factory=str)
    address: str = field(default_factory=str)
    city: str = field(default_factory=str)
    country: str = field(default_factory=str)
    property_id: str = field(default_factory=str)