import datetime
import uuid
from seedwork.domain.entities import RootAggregation
from modules.company.domain.value_objects import Seller
from seedwork.domain.value_objects import Money
from dataclasses import dataclass, field
from modules.company.domain.events import CompanyCreated


@dataclass
class Company(RootAggregation):
    id_company: uuid.UUID = field(hash=True, default=uuid.uuid4())
    name: str = field(default_factory=str)
    nit: str = field(default_factory=str)
    address: str = field(default_factory=str)
    city: str = field(default_factory=str)
    country: str = field(default_factory=str)
    created_at: datetime = field(default_factory=datetime.datetime.now)

    def create_company(self, company : "Company", property_id):
        self.name = company.name
        self.nit = company.nit
        self.address = company.address
        self.city = company.city
        self.country = company.country
        self.created_at = datetime.datetime.now()

        self.add_event(CompanyCreated(
            name = self.format_string(f"{self.name}"),
            nit = self.format_string(f"{self.nit}"),
            address =self.format_string(f"{self.address}"),
            city =self.format_string(f"{self.city}"),
            country =self.format_string(f"{self.country}"),
            property_id = property_id
        ))
    def format_string(self, string : str):
        string = string.replace("(","")
        string = string.replace(")","")
        string = string.replace("'","")
        string = string.replace(",","")
        return string
