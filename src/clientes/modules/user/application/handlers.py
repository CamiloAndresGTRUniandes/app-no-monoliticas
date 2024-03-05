import logging
from seedwork.application.handlers import Handler
from modules.user.infrastructure.dispatchers import Dispatcher


class UserDomainHandler(Handler):

    @staticmethod
    def user_created_handler(event):
        try:
            dispatcher = Dispatcher()
            dispatcher.publish_event(event, 'users-events')
        except Exception as e:
            logging.error(f"Publish error: {e}")
        