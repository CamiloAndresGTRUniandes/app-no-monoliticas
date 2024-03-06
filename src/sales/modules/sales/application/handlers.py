import logging
import pulsar
from pulsar.schema import *
from modules.sales.infrastructure.schema.v1.events import PropertySoldEvent, SaleCreatedEvent
from seedwork.application.handlers import Handler
from modules.sales.infrastructure.dispatchers import Dispatcher


class SaleDomainHandler(Handler):

    @staticmethod
    def sale_created_handler(event):
        try:
            dispatcher = Dispatcher()
            dispatcher.publish_event(event, 'sales-events', AvroSchema(SaleCreatedEvent))
        except Exception as e:
            logging.error(f"Publish error: {e}")

    @staticmethod
    def property_sold_handler(event):
        try:
            dispatcher = Dispatcher()
            dispatcher.publish_event(event, 'sales-events', AvroSchema(PropertySoldEvent))
        except Exception as e:
            logging.error(f"Publish error: {e}")