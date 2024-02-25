""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from src.propiedadesalpes.seedwork.dominio.fabricas import Fabrica
from src.propiedadesalpes.seedwork.dominio.repositorios import Repositorio
from src.propiedadesalpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from src.propiedadesalpes.seedwork.infraestructura.vistas import Vista
from src.propiedadesalpes.modulos.propiedades.dominio.entidades import Propiedad
from src.propiedadesalpes.modulos.propiedades.infraestructura.vistas import VistaPropiedad

from .repositorios import RepositorioPropiedadesPostgresSQL
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedades.__class__:
            return RepositorioPropiedadesPostgresSQL()
        else:
            raise ExcepcionFabrica(f"Fallo {obj}")
        
@dataclass
class FabricaVista(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
        if obj == Propiedad:
            return VistaPropiedad()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')