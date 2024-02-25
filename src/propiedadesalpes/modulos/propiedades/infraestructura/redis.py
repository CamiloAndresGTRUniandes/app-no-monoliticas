import redis


class RedisRepositorio:
    def __init__(self):
        self.cx=redis.Redis(host='localhost')

    def lrange(self, key, start, end):
        return self.cx.lrange(key, start, end)
    
    def linsert(self, key, where, pivot, value):
        return self.cx.linsert(key, where, pivot, value)

    def lpush(self, key, value):
        return self.cx.lpush(key, value)