import pulsar
from pulsar.schema import *

import datetime
import json
from modules.sales.domain.events import PropertySold

from seedwork.infrastructure import utils
from modules.sales.infrastructure.schema.v1.events import PropertySoldEvent, ProperySoldPayload, SaleCreatedEvent, SaleCreatedPayload
from modules.sales.infrastructure.schema.v1.commands import CreatePropertyCommand, CreatePropertyPayload

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Dispatcher:
    def _publish_message(self, message, topic, schema):
        try:
            client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
            producer = client.create_producer(topic, schema=schema)
            producer.send(message)
            client.close()
        except Exception as ex:
            print(f' ERROR: {ex}')
            raise ex

    def publish_event(self, event, topic, schema):
        if (event.__class__ is PropertySold):
            payload = ProperySoldPayload(
                property_id = event.property_id,
                sold = 1
            )
            integration_event = PropertySoldEvent(data= payload)
        else:
            payload = SaleCreatedPayload(
                name = event.name,
                price = event.price,
                currency = event.currency,
                created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                property_id = event.property_id
            )
            integration_event = SaleCreatedEvent(data= payload)
        self._publish_message(integration_event, topic, schema)

    def publish_command(self, command, topic):
        payload = CreatePropertyPayload(
            name = str(event.name),
            price = str(event.price),
            currency = str(event.currency),
            created_at = str(datetime.datetime.now()))
        integration_command = CreatePropertyPayload(data=payload)
        self._publish_message(integration_command, topic, AvroSchema(CreatePropertyCommand))
    