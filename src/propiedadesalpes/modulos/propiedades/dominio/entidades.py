import array
from datetime import datetime
import uuid
from src.propiedadesalpes.seedwork.dominio.entidades import AgregacionRaiz
from dataclasses import dataclass, field


@dataclass
class Propiedad(AgregacionRaiz):
    id_propiedad: uuid.UUID = field(hash=True, default=None)
    nombre: str = field(default_factory=str)
    descripcion: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    precio: float = field(default_factory=float)
    fecha_creacion: datetime = field(default_factory=datetime.now)
    fecha_actualizacion: datetime = field(default_factory=datetime.now)
    fecha_publicacion: datetime = field(default_factory=datetime.now)
    fecha_baja: datetime = field(default_factory=datetime.now)
    estado: int = field(default_factory=int)
    tipo: int = field(default_factory=int)
    habitaciones: int = field(default_factory=int)
    banos: int = field(default_factory=int)
    estacionamientos: int = field(default_factory=int)
    superficie: int = field(default_factory=int)
    imagen: str= field(default_factory=str)
    

    def crear_propiedad(self, propiedad: "Propiedad"):
        self.id_propiedad = uuid.uuid4()
        self.nombre = propiedad.nombre
        self.descripcion = propiedad.descripcion
        self.direccion = propiedad.direccion
        self.precio = propiedad.precio
        self.fecha_creacion = datetime.now()
        self.fecha_actualizacion = datetime.now()
        self.fecha_publicacion = datetime.now()
        self.fecha_baja = datetime.now()
        self.estado = propiedad.estado
        self.tipo = propiedad.tipo
        self.habitaciones = propiedad.habitaciones
        self.banos = propiedad.banos
        self.estacionamientos = propiedad.estacionamientos
        self.superficie = propiedad.superficie
        self.imagen = propiedad.imagen


