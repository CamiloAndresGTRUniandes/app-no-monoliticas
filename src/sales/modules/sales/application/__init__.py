from pydispatch import dispatcher
from .handlers import SaleDomainHandler

dispatcher.connect(SaleDomainHandler.sale_created_handler, signal='SaleCreatedDomain')
dispatcher.connect(SaleDomainHandler.property_sold_handler, signal='PropertySoldDomain')
