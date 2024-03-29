

from dataclasses import dataclass
from modules.sales.infrastructure.redis import RedisRepository
from seedwork.application.commands import Command, CommandHandler
from seedwork.domain.value_objects import Money
import uuid
import json
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
class CreateCacheSale(Command):
    name: str = field(default_factory=str)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)
    property_id : str = field(default_factory=str)

class CreateCachealeHandler(CreatePropertyBaseHandler):
    def handle(self, command: CreateCacheSale):
        property_dto = Sales
        property_dto.name = command.name
        property_dto.price = Money(command.price, command.currency)
        property_dto.property_id = command.property_id

        map_property = MapperProperty()
        propertyJson = map_property.entity_to_external(property_dto)
        try:
            redis = RedisRepository()
            property_ext = json.dumps(propertyJson, indent = 4)
            redis.lpush("sales", property_ext)
        except Exception as e:
            print(e)
        

@command.register(CreateCacheSale)
def execute_command_create_property(command: CreateCacheSale):
    handler = CreateCachealeHandler()
    handler.handle(command)