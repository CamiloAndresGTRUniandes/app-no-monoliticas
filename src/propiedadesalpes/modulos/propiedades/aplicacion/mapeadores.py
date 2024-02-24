from propiedadesalpes.seedwork.aplicacion.dto import DTO
from src.propiedadesalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from src.propiedadesalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from src.propiedadesalpes.modulos.propiedades.dominio.entidades import Propiedad
from .dto import PropiedadDTO

from datetime import datetime

class MapeadorPropiedadDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()
        propiedad_dto.nombre = externo['nombre']
        propiedad_dto.descripcion = externo['descripcion']
        propiedad_dto.direccion = str(externo['direccion'])
        propiedad_dto.precio = externo['precio']
        propiedad_dto.estado = externo['estado']
        propiedad_dto.imagen = str(externo['imagen'])
        propiedad_dto.fecha_creacion = externo['fecha_creacion']
        propiedad_dto.fecha_actualizacion = externo['fecha_actualizacion']
        propiedad_dto.habitaciones = externo['habitaciones']
        propiedad_dto.baños = externo['baños']
        return propiedad_dto
    
    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__
    
    
