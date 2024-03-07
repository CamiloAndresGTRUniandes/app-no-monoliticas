from seedwork.domain.repositories import Mapper
from modules.company.domain.entities import Company
from seedwork.domain.value_objects import Money
from .dto import Company as CompanyDTO



class CompanyMapper(Mapper):
    def entity_to_dto(self, entity: Company) -> CompanyDTO:
        company_dto = CompanyDTO()
        company_dto.id = entity.id
        company_dto.name = entity.name
        company_dto.nit = entity.nit
        company_dto.address = entity.address
        company_dto.city = entity.city
        company_dto.country = entity.country
        return company_dto
    
    def dto_to_entity(self, dto: CompanyDTO) -> Company:
        company_entity = Company()
        company_entity.name = dto.name
        company_entity.nit = dto.nit
        company_entity.address = dto.address
        company_entity.city = dto.city
        company_entity.country = dto.country
        return company_entity
    
    def get_type(self) -> type:
        return Company.__class__