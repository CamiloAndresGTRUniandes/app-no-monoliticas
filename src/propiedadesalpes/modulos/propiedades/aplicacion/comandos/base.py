from seedwork.aplicacion.comandos import ComandoHandler
from modulos.propiedades.infraestructura.fabricas import FabricaRepositorio, FabricaVista
from modulos.propiedades.dominio.fabricas import FabricaPropiedades

class CrearPropiedadBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_vista: FabricaVista = FabricaVista()
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades   

    @property
    def fabrica_vista(self):
        return self._fabrica_vista 
    