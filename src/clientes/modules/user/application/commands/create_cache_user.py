

from dataclasses import dataclass
import logging
import traceback
from modules.user.domain.value_objects import Name
from modules.user.infrastructure.redis import RedisRepository
from seedwork.application.commands import Command, CommandHandler
from seedwork.domain.value_objects import Money
import uuid
import json
from dataclasses import field
from modules.user.application.commands.base import CreateUserBaseHandler
from modules.user.application.dto import UserDTO

from modules.user.domain.entities import User
from modules.user.application.mappers import MapperUser
from seedwork.application.commands import execute_command as command
from seedwork.infrastructure.uow import UnitOfWorkPort

import datetime

@dataclass
class CreateCacheUser(Command):
    firstName: str = field(default_factory=str)
    lastname: str = field(default_factory=str)
    userName: str = field(default_factory=str)
    password: str = field(default_factory=str)
    created_at: str = field(default_factory=str)

class CreateCacheUserHandler(CreateUserBaseHandler):
    def handle(self, command: CreateCacheUser):
        user_dto = User(
        name = Name(command.firstName, command.lastname),
        userName = command.userName,
        password = command.password,
        created_at = command.created_at
        )
        map_user = MapperUser()
        userJson = map_user.entity_to_external(user_dto)
        try:
            redis = RedisRepository()
            user_ext = json.dumps(userJson, indent = 4)
            redis.lpush("users", user_ext)
        except Exception as e:
            logging.error(f"Pasó aqui {e}")
            traceback.print_exc
        

@command.register(CreateCacheUser)
def execute_command_create_user(command: CreateCacheUser):
    handler = CreateCacheUserHandler()
    handler.handle(command)