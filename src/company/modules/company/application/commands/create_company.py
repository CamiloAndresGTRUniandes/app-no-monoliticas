from dataclasses import dataclass
from seedwork.application.commands import Command, CommandHandler
import uuid
from dataclasses import field
from modules.company.application.commands.base import CreateCompanyBaseHandler
from modules.company.application.dto import CompanyDTO

from modules.company.domain.entities import Company
from modules.company.application.mappers import MapperCompany
from modules.company.domain.repositories import CompanyRepository
from seedwork.application.commands import execute_command as command
from seedwork.infrastructure.unit_of_work import UnitOfWorkPortCompany

import datetime

@dataclass
class CreateCompany(Command):
    id_company: str = field(default_factory=str)
    name: str = field(default_factory=str)
    nit: str = field(default_factory=str)
    address: str = field(default_factory=str)
    city: str = field(default_factory=str)
    country: str = field(default_factory=str)
    property_id: str = field(default_factory=str)

class CreateCompanyHandler(CreateCompanyBaseHandler):
    def handle(self, command: CreateCompany):
        company_dto = CompanyDTO()
        company_dto.name = command.name
        company_dto.nit = command.nit
        company_dto.address = command.address
        company_dto.city = command.city
        company_dto.country = command.country
            
        company : Company = self.companies_factory.create_object(company_dto, MapperCompany())
        company.create_company(company, command.property_id)
        repository = self.reposiroty_factory.create_object(CompanyRepository.__class__)
        UnitOfWorkPortCompany.register_batch(repository.add, company)
        UnitOfWorkPortCompany.commit()

@command.register(CreateCompany)
def execute_command_create_company(command: CreateCompany):
    handler = CreateCompanyHandler()
    handler.handle(command)