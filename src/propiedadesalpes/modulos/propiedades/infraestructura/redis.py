import redis
import os

class RedisRepositorio:
    def __init__(self):
        self.cx=redis.Redis(host=f"{os.getenv('REDIS_HOST', default='127.0.0.1')}")

    def lrange(self, key, start, end):
        return self.cx.lrange(key, start, end)
    
    def linsert(self, key, where, pivot, value):
        return self.cx.linsert(key, where, pivot, value)

    def lpush(self, key, value):
        return self.cx.lpush(key, value)
    
    def getAll(self, key):
        return self.cx.lrange(key, 0, -1)
    
    