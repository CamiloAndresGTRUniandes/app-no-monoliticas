import pulsar
from pulsar.schema import *

import datetime
import json

from seedwork.infrastructure import utils
from modules.company.infrastructure.schema.v1.events import CompanyCreatedEvent, CompanyCreatedPayload
from modules.company.infrastructure.schema.v1.commands import CreateCompanyCommand, CreateCompanyPayload

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Dispatcher:
    def _publish_message(self, message, topic, schema):
        try:
            client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
            producer = client.create_producer(topic, schema=AvroSchema(CompanyCreatedEvent))
            print("publish message @@@@@@@@@@@@@@@@@@@@@@")
            producer.send(message)
            client.close()
        except Exception as ex:
            print(f' ERROR: {ex}')
            raise ex

    def publish_event(self, event, topic):
        print("XXXXXXXXXXXXXXXXXXXXXX LLEGO A PUBLISH VVVVVVVVVVVVVVVVVVVVVVVVVVV")
        payload = CompanyCreatedPayload(
            id = str(event.id),
            name = event.name,
            nit = event.nit,
            address = event.address,
            city = event.city,
            country = event.country,
            created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            property_id = event.property_id
        )
        print(f"XXXXXXXXXXXXXXXXXXXXXX {payload} VVVVVVVVVVVVVVVVVVVVVVVVVVV")
        integration_event = CompanyCreatedEvent(data= payload)
        self._publish_message(integration_event, topic, AvroSchema(CompanyCreatedEvent))

    def publish_command(self, command, topic):
        payload = CreateCompanyPayload(
            name = str(event.name),
            price = str(event.price),
            currency = str(event.currency),
            created_at = str(datetime.datetime.now()))
        integration_command = CreateCompanyPayload(data=payload)
        self._publish_message(integration_command, topic, AvroSchema(CreateCompanyCommand))
    