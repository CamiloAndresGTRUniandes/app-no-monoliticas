import hashlib
import json
from modules.user.application.queries.login import LoginUser
from modules.user.application.queries.get_all_users import GetAllUsers
import seedwork.presentation.api as api
from modules.user.application.mappers import MapperUserDTOJson
from modules.user.application.commands.create_user import CreateUser
from seedwork.application.commands import execute_command
from seedwork.application.queries import execute_query

from flask import request, Response

from seedwork.domain.exceptions import DomainException


bp = api.create_blueprint('user', '/user')

@bp.route('', methods=['POST',])
def create_user():
    try:
        dict_property = request.json
        map_property = MapperUserDTOJson()
        user_dto = map_property.external_to_dto(dict_property)

        command = CreateUser(
            firstName=user_dto.firstName,
            lastName=user_dto.lastName,
            userName=user_dto.userName,
            password=user_dto.password
        )
        command.password = hashlib.md5(command.password.encode('utf-8')).hexdigest()
        execute_command(command)
        return Response('{}', status=202, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('', methods=('GET',))
def get_all_users():
    map_user = MapperUserDTOJson()
    query_result = execute_query(GetAllUsers())
    results = []
    
    for user in query_result.result:
        results.append(map_user.dto_to_external(user))
    
    return results

@bp.route('/login', methods=('POST',))
def login():
    try: 
        userName = request.json['userName']
        password = hashlib.md5(request.json['password'].encode('utf-8')).hexdigest()

        query_result = execute_query(LoginUser(userName=userName, password=password))
        if (query_result == 1):
            return Response('{}', status=400, mimetype='application/json')
        else:
            return {"token": query_result.result}, 200


    except Exception as e:
        print(e)