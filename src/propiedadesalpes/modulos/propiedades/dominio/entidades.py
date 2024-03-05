import array
from datetime import datetime
import uuid
from seedwork.dominio.entidades import AgregacionRaiz
from dataclasses import dataclass, field

from .eventos import PropiedadCreada




@dataclass
class Propiedad(AgregacionRaiz):
    id_propiedad: uuid.UUID = field(hash=True, default=uuid.uuid4())
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

        self.agregar_evento(PropiedadCreada(
            id_propiedad= str(self.id_propiedad), 
            nombre= str(self.nombre), 
            descripcion= str(self.descripcion), 
            direccion= str(self.direccion), 
            precio= str(self.precio), 
            fecha_creacion= str(self.fecha_creacion), 
            fecha_actualizacion= str(self.fecha_actualizacion),
            fecha_publicacion= str(self.fecha_publicacion),
            fecha_baja= str(self.fecha_baja),
            estado= str(self.estado),
            tipo= str(self.tipo),
            habitaciones= str(self.habitaciones),
            banos= str(self.banos),
            estacionamientos= str(self.estacionamientos),
            superficie= str(self.superficie),
            imagen= str(self.imagen)))


