from dataclasses import dataclass
from seedwork.application.commands import Command, CommandHandler
import uuid
from dataclasses import field
from modules.sales.application.commands.base import CreatePropertyBaseHandler
from modules.sales.application.dto import SalesDTO

from modules.sales.domain.entities import Sales
from modules.sales.application.mappers import MapperProperty
from modules.sales.domain.repositories import PropertyRepository
from seedwork.application.commands import execute_command as command
from seedwork.infrastructure.uow_sales import UnitOfWorkPortSales

import datetime

@dataclass
class CreateProperty(Command):
    name: str = field(default_factory=str)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)
    property_id : str = field(default_factory=str)

class CreatePropertyHandler(CreatePropertyBaseHandler):
    def handle(self, command: CreateProperty):
        property_dto = SalesDTO()
        property_dto.name = command.name,
        property_dto.price = command.price,
        property_dto.currency = command.currency
        property_dto.property_id = command.property_id
            
        sales : Sales = self.properties_factory.create_object(property_dto, MapperProperty())
        sales.create_sale(sales)
        sales.add_created_event()
        repository = self.reposiroty_factory.create_object(PropertyRepository.__class__)
        UnitOfWorkPortSales.register_batch(repository.add, sales)
        UnitOfWorkPortSales.commit()

@command.register(CreateProperty)
def execute_command_create_property(command: CreateProperty):
    handler = CreatePropertyHandler()
    handler.handle(command)