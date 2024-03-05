
from modules.user.infrastructure.factories import ViewFactory
from modules.user.domain.factories import UsersFactory
from seedwork.application.queries import QueryHandler

class PropertyQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._view_factory: ViewFactory = ViewFactory()
        self._properties_factory: UsersFactory = UsersFactory()

    @property
    def view_factory(self):
        return self._view_factory
    
    @property
    def properties_factory(self):
        return self._properties_factory    