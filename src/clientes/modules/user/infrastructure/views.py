

import json
from seedwork.infrastructure.views import View
from .dto import User as UserDTO
from .redis import RedisRepository




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