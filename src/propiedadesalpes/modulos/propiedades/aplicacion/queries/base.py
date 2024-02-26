from seedwork.aplicacion.queries import QueryHandler
from modulos.propiedades.infraestructura.fabricas import FabricaVista
from modulos.propiedades.dominio.fabricas import FabricaPropiedades

class ReservaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_vista: FabricaVista = FabricaVista()
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_vista(self):
        return self._fabrica_vista
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_propiedades    