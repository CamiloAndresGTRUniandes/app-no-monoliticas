
from modules.user.application.queries.base import UserQueryBaseHandler
from seedwork.application.queries import Query, QueryResult
from modules.user.domain.entities import User
from modules.user.application.dto import UserDTO
from seedwork.application.queries import execute_query as query
from dataclasses import dataclass


@dataclass
class LoginUser(Query):
    userName:str
    password:str


class LoginUserHandler(UserQueryBaseHandler):
    def handle(self, query) -> QueryResult:
        token = None
        view = self.view_factory.create_object(User)
        token = view.login(query.userName, query.password)
        return QueryResult(result = token)
    
@query.register(LoginUser)
def ejecutar_query_login(query: LoginUser):
    handler = LoginUserHandler()
    return handler.handle(query)