
from modules.company.application.queries.base import CompanyQueryBaseHandler
from seedwork.application.queries import Query, QueryHandler, QueryResult
from modules.company.domain.entities import Company
from modules.company.application.dto import CompanyDTO
from seedwork.application.queries import execute_query as query
from dataclasses import dataclass


@dataclass
class GetAllProperties(Query):
    ...


class GetAllPropertiesHandler(CompanyQueryBaseHandler):
    def handle(self, query) -> QueryResult:
        companies_dto = []
        view = self.view_factory.create_object(Company)
        companies = view.get_all()

        for company in companies:
            dto = CompanyDTO()
            dto.id_company = company.id
            dto.name = company.name
            dto.nit = company.nit
            dto.address = company.address
            dto.city = company.city
            dto.country = company.country
            companies_dto.append(dto)
        return QueryResult(companies_dto)
    
@query.register(GetAllProperties)
def ejecutar_query_obtener_propiedad(query: GetAllProperties):
    handler = GetAllPropertiesHandler()
    return handler.handle(query)