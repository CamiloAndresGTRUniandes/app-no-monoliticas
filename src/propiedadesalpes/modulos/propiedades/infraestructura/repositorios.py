""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from config.db import db
from modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from modulos.propiedades.dominio.entidades import Propiedad
from modulos.propiedades.dominio.fabricas import FabricaPropiedades
from .dto import Propiedad as PropiedadDTO
from .mapeadores import MappeadorPropiedad
from uuid import UUID

class RepositorioPropiedadesPostgresSQL(RepositorioPropiedades):
    def __init__(self):
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    def agregar(self, propiedad: Propiedad):
            propiedad_dto = self._fabrica_propiedades.crear_objeto(propiedad, MappeadorPropiedad())
            db.session.add(propiedad_dto)

    def actualizar(self, propiedad : Propiedad):
            self._fabrica_propiedades.crear_objeto(propiedad, MappeadorPropiedad())
            db.session.commit()
            
    
    def obtener_todos(self) -> list[Propiedad]:
        propiedades_list = db.session.query(Propiedad).all()
        return propiedades_list
    
    def obtener_tipo(self) -> type:
        return Propiedad.__class__
    
    def obtener_por_id(self, id: str) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=id).one()
        return self._fabrica_propiedades.crear_objeto(propiedad_dto, MappeadorPropiedad())
    
class RepositorioPropiedadesRedis(RepositorioPropiedades):
    def __init__(self):
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    def agregar(self, propiedad: Propiedad):
        ...
        