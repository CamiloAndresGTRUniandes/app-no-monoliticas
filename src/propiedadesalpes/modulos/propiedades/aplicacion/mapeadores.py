from seedwork.aplicacion.dto import Mapeador as AppMap
from seedwork.dominio.repositorios import Mapeador as RepMap
from modulos.propiedades.dominio.entidades import Propiedad
from .dto import PropiedadDTO

from datetime import datetime

class MapeadorPropiedadDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()
        propiedad_dto.nombre = externo.get("nombre")
        propiedad_dto.descripcion = externo.get("descripcion")
        propiedad_dto.direccion = externo.get("direccion")
        propiedad_dto.precio = externo.get("precio")
        propiedad_dto.estado = externo.get("estado")
        propiedad_dto.imagen = externo.get("imagen")
        propiedad_dto.fecha_creacion = datetime.now()
        propiedad_dto.fecha_actualizacion = datetime.now()
        propiedad_dto.habitaciones = externo.get("habitaciones")
        propiedad_dto.banos = externo.get("banos")
        return propiedad_dto
    
    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__


class MapeadorPropiedad(RepMap):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"
    def obtener_tipo(self) -> type:
        return Propiedad.__class__ 
    
    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()
        propiedad_dto.id_propiedad = entidad.id
        propiedad_dto.nombre = entidad.nombre
        propiedad_dto.descripcion = entidad.descripcion
        propiedad_dto.tipo = entidad.tipo
        propiedad_dto.estado = entidad.estado
        propiedad_dto.imagen = entidad.imagen
        propiedad_dto.fecha_creacion = entidad.fecha_creacion
        propiedad_dto.fecha_actualizacion = entidad.fecha_actualizacion
        propiedad_dto.habitaciones = entidad.habitaciones
        propiedad_dto.banos = entidad.banos
        propiedad_dto.precio = entidad.precio
        propiedad_dto.superficie = entidad.superficie
        propiedad_dto.direccion = entidad.direccion
        return propiedad_dto
    
    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        propiedad.nombre=dto.nombre
        propiedad.descripcion=dto.descripcion
        propiedad.tipo=dto.tipo 
        propiedad.estado=dto.estado 
        propiedad.fecha_creacion=dto.fecha_creacion 
        propiedad.fecha_actualizacion=dto.fecha_actualizacion 
        propiedad.habitaciones=dto.habitaciones 
        propiedad.precio= dto.precio 
        propiedad.superficie= dto.superficie
        propiedad.direccion=dto.direccion
        propiedad.imagen=dto.imagen
        propiedad.banos =dto.banos
        return propiedad
    
    def entidad_a_externo(self, dto: Propiedad) -> dict:
        dto._id = str(dto._id)
        dto.id_propiedad = str(dto.id_propiedad)
        dto.fecha_creacion = str(dto.fecha_creacion)
        dto.fecha_actualizacion = str(dto.fecha_actualizacion)
        dto.fecha_baja = str(dto.fecha_baja)
        dto.fecha_publicacion = str(dto.fecha_publicacion)
        return dto.__dict__