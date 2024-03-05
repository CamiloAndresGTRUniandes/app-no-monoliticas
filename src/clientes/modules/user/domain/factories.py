from dataclasses import dataclass
from seedwork.domain.factory import Factory
from seedwork.domain.repositories import Mapper
from seedwork.domain.entities import Entity
from modules.user.domain.entities import User


@dataclass
class UsersFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            user: User = mapper.dto_to_entity(obj)
            return user