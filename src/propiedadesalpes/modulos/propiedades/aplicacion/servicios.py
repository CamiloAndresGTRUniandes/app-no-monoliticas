from seedwork.aplicacion.servicios import Servicio
from modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from modulos.propiedades.dominio.fabricas import FabricaPropiedades
from modulos.propiedades.dominio.entidades import Propiedad
from modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from seedwork.infraestructura.uow import UnidadTrabajoPuerto

from .dto import PropiedadDTO
from .mapeadores import MapeadorPropiedad

class ServicioPropiedad(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio 
    
    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades
    
    def crear_propiedad(self, dto: PropiedadDTO) -> PropiedadDTO:
        propiedad : Propiedad = self._fabrica_propiedades.crear_objeto(dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.commit()

        return self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())
    
    def obtener_propiedad_por_id(self, id) -> PropiedadDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        return self._fabrica_propiedades.crear_objeto(repositorio.obtener_por_id(id), MapeadorPropiedad())