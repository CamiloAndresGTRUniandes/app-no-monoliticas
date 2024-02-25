import array
from dataclasses import dataclass, field
import datetime
from propiedadesalpes.seedwork.aplicacion.comandos import Comando


@dataclass
class CrearPropiedad(Comando):
    nombre: str
    descripcion: str
    direccion: str
    precio: float
    fecha_creacion: datetime = field(default_factory=datetime.now)
    fecha_actualizacion: datetime = field(default_factory=datetime.now)
    fecha_publicacion: datetime = field(default_factory=datetime.now)
    fecha_baja: datetime = field(default_factory=datetime.now)
    estado: int = 1
    tipo: int = 1
    habitaciones: int = 1
    banos: int = 1
    estacionamientos: int = 0
    superficie: int = 0
    imagen: list[str] = field(default_factory=list[str])
