import pulsar
from pulsar.schema import *

import datetime
import json

from seedwork.infrastructure import utils
from modules.user.infrastructure.schema.v1.events import UserCreatedEvent, UserCreatedPayload
from modules.user.infrastructure.schema.v1.commands import CreateUserCommand, CreateUserPayload

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Dispatcher:
    def _publish_message(self, message, topic, schema):
        try:
            client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
            producer = client.create_producer(topic, schema=AvroSchema(UserCreatedEvent))
            producer.send(message)
            client.close()
        except Exception as ex:
            print(f' ERROR: {ex}')
            raise ex

    def publish_event(self, event, topic):
        payload = UserCreatedPayload(
            firstName = event.first_name,
            lastName = event.last_name,
            userName = event.user_name,
            created_at = str(datetime.datetime.now())
        )
        integration_event = UserCreatedEvent(data= payload)
        self._publish_message(integration_event, topic, AvroSchema(UserCreatedEvent))

    def publish_command(self, command, topic):
        payload = CreateUserPayload(
            firstName = command.first_name,
            lastName = command.last_name,
            userName = command.user_name,
            created_at = str(datetime.datetime.now()))
        integration_command = CreateUserPayload(data=payload)
        self._publish_message(integration_command, topic, AvroSchema(CreateUserCommand))
    