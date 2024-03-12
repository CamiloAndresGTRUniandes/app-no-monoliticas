import json
import time
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback

from modules.company.application.commands.create_cache_company import CreateCacheCompany
from modules.company.infrastructure.schema.v1.commands import CreateCompanyCommand
from seedwork.application.commands import execute_command
from modules.company.infrastructure.schema.v1.events import CompanyCreatedEvent

from seedwork.infrastructure import utils

def subscribe_to_events():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('company-events', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='companies-sub-events', schema=AvroSchema(CompanyCreatedEvent))
        
        while True:
            message = consumer.receive()
            ex = message.value()
            company_dto = ex.data
            print(f'EVENT RECEIVED IN COMPANY: {company_dto}')
            command = CreateCacheCompany(
                name=company_dto.name,
                nit=company_dto.nit,
                address=company_dto.address,
                city=company_dto.city,
                country= company_dto.country)
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
        consumer = client.subscribe('company-commands', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='companies-sub-commands', schema=AvroSchema(CreateCompanyCommand))

        while True:
            message = consumer.receive()
            ex = message.value()
            company_dto = ex.data
            command = CreateCacheCompany(
                name=company_dto.name,
                price=company_dto.price,
                currency=company_dto.currency,
                seller=company_dto.seller
                )
            execute_command(command)
            consumer.acknowledge(message)     
            
        client.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if client:
            client.close()