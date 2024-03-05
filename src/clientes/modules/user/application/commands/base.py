
from modules.user.infrastructure.factories import ReposirotyFactory 
from seedwork.application.commands import CommandHandler
from modules.user.domain.factories import UsersFactory


class CreateUserBaseHandler(CommandHandler):
    def __init__(self):
        self._reposiroty_factory: ReposirotyFactory = ReposirotyFactory()
        self._users_factory: UsersFactory = UsersFactory()

    @property
    def reposiroty_factory(self):
        return self._reposiroty_factory
    
    @property
    def properties_factory(self):
        return self._users_factory    
    