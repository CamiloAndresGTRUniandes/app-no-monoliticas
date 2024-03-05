import json
from modules.user.application.queries.get_all_users import GetAllUsers
import seedwork.presentation.api as api
from modules.user.application.mappers import MapperUserDTOJson
from modules.user.application.commands.create_user import CreateUser
from seedwork.application.commands import execute_command
from seedwork.application.queries import execute_query

from flask import request, Response

from seedwork.domain.exceptions import DomainException


bp = api.create_blueprint('property', '/property')

@bp.route('', methods=['POST',])
def create_user():
    try:
        dict_property = request.json
        map_property = MapperUserDTOJson()
        user_dto = map_property.external_to_dto(dict_property)

        command = CreateUser(
            firstname=user_dto.firstname,
            lastname=user_dto.lastname,
            username=user_dto.username,
            password=user_dto.password
        )
        execute_command(command)
        return Response('{}', status=202, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('', methods=('GET',))
def get_all_properties():
    map_user = MapperUserDTOJson()
    query_result = execute_query(GetAllUsers())
    results = []
    
    for user in query_result.result:
        results.append(map_user.dto_to_external(user))
    
    return results