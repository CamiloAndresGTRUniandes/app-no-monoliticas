import json
import time
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback

from modules.sales.application.commands.create_cache_property import CreateCacheSale
from modules.sales.infrastructure.schema.v1.commands import CreatePropertyCommand
from seedwork.application.commands import execute_command
from modules.sales.infrastructure.schema.v1.events import SaleCreatedEvent

from seedwork.infrastructure import utils

def subscribe_to_events():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('sales-events', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='sales-sub-events', schema=AvroSchema(SaleCreatedEvent))
        
        while True:
            message = consumer.receive()
            ex = message.value()
            property_dto = ex.data
            print(f'EVENT RECEIVED SALE CREATED EVENT: {property_dto}')
            command = CreateCacheSale(
                name=property_dto.name,
                price=property_dto.price,
                currency=property_dto.currency,
                property_id=property_dto.property_id)
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
        consumer = client.subscribe('sales-commands', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='sales-sub-commands', schema=AvroSchema(CreatePropertyCommand))

        while True:
            message = consumer.receive()
            ex = message.value()
            property_dto = ex.data
            print(f'COMMAND RECEIVED SALE CREATED COMMAND: {property_dto}')
            command = CreateCacheSale(
                name=property_dto.name,
                price=property_dto.price,
                currency=property_dto.currency,
                property_id=property_dto.property_id
                )
            execute_command(command)
            consumer.acknowledge(message)     
            
        client.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if client:
            client.close()