from src.propiedadesalpes.seedwork.aplicacion.servicios import Servicio
from src.propiedadesalpes.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from src.propiedadesalpes.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from src.propiedadesalpes.modulos.propiedades.dominio.entidades import Propiedad
from src.propiedadesalpes.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from src.propiedadesalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto

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
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())