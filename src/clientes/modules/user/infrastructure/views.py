

import json
from seedwork.infrastructure.views import View
from .dto import User as UserDTO
from .redis import RedisRepository
from config.db import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity



class UserView(View):
    def get_all(self):
        users = list()
        redis = RedisRepository()
        propiedadesRedis = redis.lrange('users', 0, -1)
        for propertyRedis in propiedadesRedis:
            propertyDto = json.loads(propertyRedis)

            users.append(UserDTO(
                firstName = propertyDto['firstName'],
                lastName = propertyDto['lastName'],
                userName = propertyDto['userName'],
                created_at = propertyDto['created_at']
                ))

        return users
    
    def get_by(self, id=None, estado=None, id_cliente=None, **kwargs):
        raise NotImplementedError('Not Implemented')
    
    def login(self, userName, password):
        user = None
        user = db.session.query(UserDTO).filter(UserDTO.userName == userName,  UserDTO.password == password).first()
        print(f"Resturned user: {user}")
        db.session.close()
        if (user is None):
            return 1
        else:
            token = create_access_token(identity= user.id)
            return token
