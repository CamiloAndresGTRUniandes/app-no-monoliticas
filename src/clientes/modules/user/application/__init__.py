from pydispatch import dispatcher
from .handlers import UserDomainHandler

dispatcher.connect(UserDomainHandler.user_created_handler, signal='UserCreatedDomain')
