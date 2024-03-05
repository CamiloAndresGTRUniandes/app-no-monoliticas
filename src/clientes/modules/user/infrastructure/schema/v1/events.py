from dataclasses import field
from pulsar.schema import *

from seedwork.infrastructure.schema.v1.events import IntegrationEvent

class UserCreatedPayload(Record):
    firstName = String()
    lastName = String()
    userName = String()
    password = String()
    created_at = String()

class UserCreatedEvent(IntegrationEvent):
    data = UserCreatedPayload()