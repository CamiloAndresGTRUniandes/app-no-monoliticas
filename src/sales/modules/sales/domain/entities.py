import datetime
import uuid
from seedwork.domain.entities import RootAggregation
from modules.sales.domain.value_objects import Seller
from seedwork.domain.value_objects import Money
from dataclasses import dataclass, field
from modules.sales.domain.events import PropertySold, SaleCreated


@dataclass
class Sales(RootAggregation):
    sale_id: uuid.UUID = field(hash=True, default=uuid.uuid4())
    property_id: str = field(default_factory=str)
    name: str = field(default_factory=str)
    price: Money = field(default_factory=Money)
    created_at: datetime = field(default_factory=datetime.datetime.now)

    def create_sale(self, sales : "Sales"):
        self.name = sales.name
        self.price = Money(amount=sales.price.amount, currency=sales.price.currency)
        self.property_id = sales.property_id
        self.created_at = datetime.datetime.now()

        self.add_event(PropertySold(
            property_id = self.property_id,
            sold= 1
        ))
    def format_string(self, string : str):
        string = string.replace("(","")
        string = string.replace(")","")
        string = string.replace("'","")
        string = string.replace(",","")
        return string
    
    def add_created_event(self):
        self.add_event(SaleCreated(
            name = self.format_string(f"{self.name}"),
            price = self.format_string(f"{self.price.amount}"),
            currency =self.format_string(f"{self.price.currency}"),
            property_id = self.property_id
        ))
