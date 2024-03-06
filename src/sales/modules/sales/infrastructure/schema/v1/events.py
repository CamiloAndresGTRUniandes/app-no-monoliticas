from dataclasses import field
from pulsar.schema import *

from seedwork.infrastructure.schema.v1.events import IntegrationEvent

class SaleCreatedPayload(Record):

    property_id = String()
    name = String()
    price = String()
    currency = String()
    created_at = String()

class SaleCreatedEvent(IntegrationEvent):
    data = SaleCreatedPayload()


class ProperySoldPayload(Record):

    property_id = String()
    sold = String

class PropertySoldEvent(IntegrationEvent):
    data = ProperySoldPayload()