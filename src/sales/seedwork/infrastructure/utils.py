import time
import os

def time_millis():
    return int(time.time() * 1000)

def broker_host():
    return os.getenv('BROKER_HOST', default='127.0.0.1')

def broker_rabbit_host():
    return os.getenv('RABBITMQ_HOST', default='127.0.0.1')

def broker_rabbit_port():
    return os.getenv('RABBITMQ_PORT', default='5672')

def broker_rabbit_user():
    return os.getenv('RABBITMQ_USER', default='rabbitmq')
    
def broker_rabbit_password():
    return os.getenv('RABBITMQ_PASS', default='LosAndes1234')

def database_connection_string():
    return f"postgresql://{os.environ.get('DB_USER', default='postgres')}:{os.environ.get('DB_PASSWORD', default='LosAndes1234')}@{os.environ.get('DB_HOST', default='127.0.0.1')}:{os.environ.get('DB_PORT', default='5432')}/{os.environ.get('DB_NAME', default='sales')}"

def redis_host():
    return f"{os.getenv('REDIS_HOST', default='127.0.0.1')}"


