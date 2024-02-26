""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from seedwork.dominio.repositorios import Mapeador
from modulos.propiedades.dominio.entidades import Propiedad
from .dto import Propiedad as PropiedadDTO


    
class MappeadorPropiedad(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        
        propiedad_dto = PropiedadDTO()
        propiedad_dto.id = entidad.id
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
        propiedad.banos=dto.banos

        return propiedad
    
    def obtener_tipo(self) -> type:
        return Propiedad.__class__