from seedwork.application.dto import Mapper as AppMap
from seedwork.domain.repositories import Mapper as RepMap
from modules.company.application.dto import CompanyDTO
from modules.company.domain.entities import Company
from seedwork.domain.value_objects import Money

class MapperCompanyDTOJson(AppMap):
    def external_to_dto(self, external: dict) -> CompanyDTO:
        company_dto = CompanyDTO()
        company_dto.name = external.get('name'),
        company_dto.nit = external.get('nit'),
        company_dto.address = external.get('address'),
        company_dto.city = external.get('city'),
        company_dto.country = external.get('country')
        return company_dto
    

    def dto_to_external(self, dto: CompanyDTO) -> dict:
        return dto.__dict__
    
class MapperCompany(RepMap):
    def get_type(self) -> type:
        return CompanyDTO.__class__

    def dto_to_entity(self, dto: CompanyDTO) -> Company:
        company_entity = Company()
        company_entity.name = dto.name
        company_entity.nit = dto.nit
        company_entity.address = dto.address
        company_entity.city = dto.city
        company_entity.country = dto.country
        return company_entity
    
    def entity_to_dto(self, entity: Company) -> CompanyDTO:
        company_dto = CompanyDTO()
        company_dto.id_company = entity.id
        company_dto.name = entity.name
        company_dto.nit = entity.nit
        company_dto.address = entity.address
        company_dto.city = entity.city
        company_dto.country = entity.country

    
    def entity_to_external(self, entity: Company) -> dict:
        return {
            "company_id" : f"{entity.id_company}",
            "name" : f"{entity.name}",
            "nit" : f"{entity.nit}",
            "address" : f"{entity.address}",
            "city" : f"{entity.city}",
            "country" : f"{entity.country}",
        }
    
    def external_to_entity(self, external: dict) -> Company:
        company_entity = Company()
        company_entity.name= external.get('name')
        company_entity.nit = external.get('nit')
        company_entity.address = external.get('address')
        company_entity.city = external.get('city')
        company_entity.country = external.get('country')

        return company_entity
    