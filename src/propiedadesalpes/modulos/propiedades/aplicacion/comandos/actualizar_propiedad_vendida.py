from dataclasses import dataclass, field
from datetime import datetime
from seedwork.aplicacion.comandos import Comando
from modulos.propiedades.aplicacion.dto import PropiedadDTO
from modulos.propiedades.dominio.entidades import Propiedad
from modulos.propiedades.aplicacion.comandos.base import CrearPropiedadBaseHandler
from modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from seedwork.infraestructura.unit_of_work_prop import UnidadTrabajoPuerto
from seedwork.aplicacion.comandos import ejecutar_commando as comando

@dataclass
class ActualizarPropiedadVendida(Comando):
    id : str = field(default_factory=str)
    vendido : int = field(default_factory=int)

class ActualizarPropiedadVendidaHandler(CrearPropiedadBaseHandler):
    def handle(self, comando: ActualizarPropiedadVendida):
        vista = self.fabrica_vista.crear_objeto(Propiedad)

        propiedad: Propiedad =  self.fabrica_propiedades.crear_objeto(vista.obtener_por(id=comando.id)[0], MapeadorPropiedad())
        propiedad.actualizar_propiedad_vendida(comando.vendido)

        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, propiedad)
        UnidadTrabajoPuerto.commit()

@comando.register(ActualizarPropiedadVendida)
def ejecutar_comando_actualizar_propiedad_vendida(comando: ActualizarPropiedadVendida):
    handler = ActualizarPropiedadVendidaHandler()
    handler.handle(comando)