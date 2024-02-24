

from dataclasses import dataclass
from enum import Enum


@dataclass
class Estado(Enum):
    Activo = 1
    Inactivo = 2

@dataclass
class TipoPropiedad(Enum):
    Casa = 1
    Departamento = 2
    Terreno = 3
    Oficina = 4
    Local = 5
    Garage = 6
    Bodega = 7
    Edificio = 8
    Hotel = 9