from dataclasses import dataclass
from seedwork.application.commands import Command, CommandHandler
import uuid
from dataclasses import field
from modules.user.application.commands.base import CreateUserBaseHandler
from modules.user.application.dto import UserDTO

from modules.user.domain.entities import User
from modules.user.application.mappers import MapperUser
from modules.user.domain.repositories import UserRepository
from seedwork.application.commands import execute_command as command
from seedwork.infrastructure.uow import UnitOfWorkPort

import datetime

@dataclass
class CreateUser(Command):
    firstName: str = field(default_factory=str)
    lastName: str = field(default_factory=str)
    userName: str = field(default_factory=str)
    password: str = field(default_factory=str)

class CreateUserHandler(CreateUserBaseHandler):
    def handle(self, command: CreateUser):
        user_dto = UserDTO()
        user_dto.firstName = command.firstName
        user_dto.lastName = command.lastName
        user_dto.userName = command.userName
        user_dto.password = command.password
        print(f"En create User: {user_dto}")
        user : User = self._users_factory.create_object(user_dto, MapperUser())
        user.create_property(user)
        repository = self.reposiroty_factory.create_object(UserRepository.__class__)
        UnitOfWorkPort.register_batch(repository.add, user)
        UnitOfWorkPort.commit()

@command.register(CreateUser)
def execute_command_create_property(command: CreateUser):
    handler = CreateUserHandler()
    handler.handle(command)