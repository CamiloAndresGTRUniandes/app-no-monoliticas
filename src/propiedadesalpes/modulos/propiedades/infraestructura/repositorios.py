""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from propiedadesalpes.config.db import db
from propiedadesalpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from propiedadesalpes.modulos.propiedades.dominio.entidades import Propiedad
from propiedadesalpes.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from .dto import Reserva as ReservaDTO
from .mapeadores import MapeadorReserva
from uuid import UUID

class RepositorioPropiedadesPostgresSQL(RepositorioPropiedades):
    def __init__(self):
        self._fabrica_vuelos: FabricaPropiedades = FabricaPropiedades()

    def agregar(self, propiedad: Propiedad):
        reserva_dto = self.fabrica_vuelos.crear_objeto(propiedad, MapeadorReserva())
        db.session.add(reserva_dto)
    
    def obtener_todos(self) -> list[Propiedad]:
        propiedades_list = db.session.query(Propiedad).all()
        return propiedades_list