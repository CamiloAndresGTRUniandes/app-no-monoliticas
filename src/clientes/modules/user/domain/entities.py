import datetime
import uuid
from seedwork.domain.entities import RootAggregation
from modules.user.domain.value_objects import Name
from seedwork.domain.value_objects import Money
from dataclasses import dataclass, field
from modules.user.domain.events import  userCreated


@dataclass
class User(RootAggregation):
    id_user: uuid.UUID = field(hash=True, default=uuid.uuid4())
    name: Name = field(default_factory=Name)
    userName : str = field(default_factory=str)
    password : str = field(default_factory=str)
    created_at: datetime = field(default_factory=datetime.datetime.now)

    def create_property(self, user : "User"):
        self.name = Name(user.name.firstName, user.name.lastName)
        self.userName = user.userName
        self.password = user.password
        self.created_at = datetime.datetime.now()

        self.add_event(userCreated(
            firstName = self.format_string(f"{self.name.firstName}"),
            lastName = self.format_string(f"{self.name.lastName}"),
            userName = self.format_string(f"{self.userName}"),
            password = f"{self.password}",
        ))
    def format_string(self, string : str):
        string = string.replace("(","")
        string = string.replace(")","")
        string = string.replace("'","")
        string = string.replace(",","")
        return string
