from dataclasses import dataclass, field

from seedwork.domain.events import (DomainEvent)


@dataclass
class SaleCreated(DomainEvent):
    name : str = field(default_factory = str)
    description : str = field(default_factory = str)
    price : str = field(default_factory = str)
    currency : str = field(default_factory = str)
    property_id : str = field(default_factory = str)
    created_at : str = field(default_factory = str)

@dataclass
class PropertySold(DomainEvent):
    sold : int = field(default_factory = int)
    property_id : str = field(default_factory = str)
