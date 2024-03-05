from config.db import db
from modules.user.domain.factories import UsersFactory
from modules.user.domain.repositories import UserRepository
from modules.user.domain.entities import User
from seedwork.domain.entities import Entity
from .mappers import UserMapper


class UsersPostgresSQLRepository(UserRepository):
    def __init__(self):
        self.users_factory : UsersFactory = UsersFactory()

    def add(self, user: User):
        user_dto = self.users_factory.create_object(user, UserMapper())
        db.session.add(user_dto)

    def get_all(self) -> list[User]:
        user_dto = db.session.query(User).all()
        return user_dto
    
    def get_by_id(self, id: int) -> User:
        user_dto = db.session.query(User).filter_by(id=id).first()
        return self.users_factory.create_object(user_dto, UserMapper())
    
    def get_type(self) -> type:
        return User.__class__
    
    def delete(self, id: int):
        user_dto = db.session.query(User).filter_by(id=id).first()
        db.session.delete(user_dto)

    def update(self, entity: Entity):
        raise NotImplementedError
