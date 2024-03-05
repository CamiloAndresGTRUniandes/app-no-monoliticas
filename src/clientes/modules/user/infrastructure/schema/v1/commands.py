from pulsar.schema import *
from dataclasses import dataclass, field
from seedwork.infrastructure.schema.v1.commands import (IntegrationCommand)

class CreateUserPayload(IntegrationCommand):
    firstName = String()
    lastName = String()
    userName = String()
    password = String()
    created_at = String()

class CreateUserCommand(IntegrationCommand):
    data = CreateUserPayload()