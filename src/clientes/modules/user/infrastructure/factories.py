


from dataclasses import dataclass
from modules.user.infrastructure.views import UserView
from seedwork.infrastructure.views import View
from modules.user.domain.entities import User

from seedwork.domain.factory import Factory
from seedwork.domain.repositories import Repository
from modules.user.domain.repositories import UserRepository
from .repositories import UsersPostgresSQLRepository
from .exceptions import FactoryException


@dataclass
class ReposirotyFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == UserRepository.__class__:
            return UsersPostgresSQLRepository()
        else:
            raise FactoryException(f"Error {obj}")
        
@dataclass
class ViewFactory(Factory):
    def create_object(self, obj: type, mapeador: any = None) -> View:
        if obj == User:
            return UserView()
        else:
            raise FactoryException(f'Not Implemented {obj}')