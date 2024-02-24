import array
from datetime import datetime
import uuid
from src.propiedadesalpes.seedwork.dominio.entidades import Entidad, AgregacionRaiz
from dataclasses import dataclass, field

from .enumerations import Estado, TipoPropiedad
from .objetos_valor import Nombre, Email, Descripcion, Direccion

@dataclass
class Propiedad(AgregacionRaiz):
    id_propiedad = uuid.UUID(hash=True, default=None)
    nombre: Nombre = field(default_factory=Nombre)
    descripcion: Descripcion = field(default_factory=Descripcion)
    direccion: Direccion = field(default_factory=Direccion)
    precio: float
    fecha_creacion: datetime = field(default_factory=datetime.now)
    fecha_actualizacion: datetime = field(default_factory=datetime.now)
    fecha_publicacion: datetime = field(default_factory=datetime.now)
    fecha_baja: datetime = field(default_factory=datetime.now)
    estado: Estado = 1
    tipo: TipoPropiedad = 1
    habitaciones: int = 1
    baños: int = 1
    estacionamientos: int = 0
    superficie: int = 0
    imagen: list[str] = field(default_factory=list[str])
    


