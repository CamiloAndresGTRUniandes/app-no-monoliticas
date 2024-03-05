from modules.user.domain.value_objects import Name
from seedwork.application.dto import Mapper as AppMap
from seedwork.domain.repositories import Mapper as RepMap
from modules.user.application.dto import UserDTO
from modules.user.domain.entities import User

class MapperUserDTOJson(AppMap):
    def external_to_dto(self, external: dict) -> UserDTO:
        user_dto = UserDTO()
        user_dto.firstName = external.get('firstName')
        user_dto.lastName = external.get('lastName')
        user_dto.userName = external.get('userName')
        user_dto.password = external.get('password')
        return user_dto
    

    def dto_to_external(self, dto: UserDTO) -> dict:
        return dto.__dict__
    
class MapperUser(RepMap):
    def get_type(self) -> type:
        return UserDTO.__class__

    def dto_to_entity(self, dto: UserDTO) -> User:
        user_entity = User()
        user_entity.name = Name(dto.firstName, dto.lastName)
        user_entity.userName = dto.userName
        user_entity.password = dto.password
        return user_entity
    
    def entity_to_dto(self, entity: User) -> UserDTO:
        user_dto = UserDTO()
        user_dto.id_user=entity.id
        user_dto.firstName=entity.name.firstName
        user_dto.firstName=entity.name.firstName
        user_dto.userName=entity.userName
        user_dto.password=entity.password

    
    def entity_to_external(self, entity: User) -> dict:
        return {
            "id_user": entity.id,
            "firstName": entity.name.firstName,
            "lastName": entity.name.lastName,
            "userName": entity.userName,
            "created_at": entity.created_at
        }
    
    def external_to_entity(self, external: dict) -> User:
        user_entity = User()
        user_entity.name= Name(external.get('firstName'), external.get('lastName'))
        user_entity.userName = external.get('userName')
        user_entity.password = external.get('password')

        return user_entity
    