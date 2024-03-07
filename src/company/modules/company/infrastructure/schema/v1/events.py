from dataclasses import field
from pulsar.schema import *

from seedwork.infrastructure.schema.v1.events import IntegrationEvent

class CompanyCreatedPayload(Record):
    id = String()
    name = String()
    nit = String()
    address = String()
    city = String()
    country = String()
    created_at: String()
    property_id = String()

class CompanyCreatedEvent(IntegrationEvent):
    data = CompanyCreatedPayload()