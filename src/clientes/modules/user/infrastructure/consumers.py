import json
import time
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback

from modules.user.application.commands.create_cache_user import CreateCacheUser
from modules.user.infrastructure.schema.v1.commands import CreateUserCommand
from seedwork.application.commands import execute_command
from modules.user.infrastructure.schema.v1.events import UserCreatedEvent

from seedwork.infrastructure import utils

def subscribe_to_events():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('users-events', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='users-sub-events', schema=AvroSchema(UserCreatedEvent))
        print('Subscribed to events')
        while True:
            message = consumer.receive()
            ex = message.value()
            user_dto = ex.data
            print(f'EVENT RECEIVED: {user_dto}')
            command = CreateCacheUser(
                firstName=user_dto.firstName,
                lastname=user_dto.lastName,
                userName=user_dto.userName,
                created_at=user_dto.created_at
                )
            execute_command(command)
            consumer.acknowledge(message)     

        client.close()
    except Exception as e:
        logging.error(f'ERROR: Subscribing to events topic!: {e}')
        traceback.print_exc()
        if client:
            client.close()

def subscribe_to_commands():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('users-commands', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='users-sub-commands', schema=AvroSchema(CreateUserCommand))

        while True:
            message = consumer.receive()
            ex = message.value()
            user_dto = ex.data
            print(f'COMMAND RECEIVED: {user_dto}')
            command = CreateCacheUser(
                firstName=user_dto.firstName,
                lastname=user_dto.lastName,
                userName=user_dto.userName,
                created_at=user_dto.created_at
                )
            execute_command(command)
            consumer.acknowledge(message)     
            
        client.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if client:
            client.close()