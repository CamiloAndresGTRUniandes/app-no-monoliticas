
from modules.user.application.queries.base import PropertyQueryBaseHandler
from seedwork.application.queries import Query, QueryResult
from modules.user.domain.entities import User
from modules.user.application.dto import UserDTO
from seedwork.application.queries import execute_query as query
from dataclasses import dataclass


@dataclass
class GetAllUsers(Query):
    ...


class GetAllPropertiesHandler(PropertyQueryBaseHandler):
    def handle(self, query) -> QueryResult:
        users_dto = []
        view = self.view_factory.create_object(User)
        users = view.get_all()

        for user in users:
            dto = UserDTO()
            dto.id_user = user.id_user
            dto.firstName = user.firstName
            dto.lastName = user.lastName
            dto.userName = user.userName
            dto.created_at = user.created_at
            
            users_dto.append(dto)
        return QueryResult(users_dto)
    
@query.register(GetAllUsers)
def ejecutar_query_obtener_propiedad(query: GetAllUsers):
    handler = GetAllPropertiesHandler()
    return handler.handle(query)