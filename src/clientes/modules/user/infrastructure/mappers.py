from modules.user.domain.value_objects import Name
from seedwork.domain.repositories import Mapper
from modules.user.domain.entities import User
from seedwork.domain.value_objects import Money
from .dto import User as UserDTO



class UserMapper(Mapper):
    def entity_to_dto(self, entity: User) -> UserDTO:
        user_dto = UserDTO()
        user_dto.id = entity.id
        user_dto.firstName = entity.name.firstName
        user_dto.lastName = entity.name.lastName
        user_dto.userName = entity.userName
        user_dto.password = entity.password
        user_dto.created_at = entity.created_at
        return user_dto
    
    def dto_to_entity(self, dto: UserDTO) -> User:
        user_entity = User(
        name = Name(dto.firstName, dto.lastName),
        userName = dto.userName,
        password = dto.password)
        return user_entity
    
    def get_type(self) -> type:
        return User.__class__