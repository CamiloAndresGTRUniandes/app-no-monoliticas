from dataclasses import dataclass, field
from src.propiedadesalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class PropiedadDTO(DTO):
    id_propiedad: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    descripcion: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    precio: float = field(default_factory=float)
    tipo: int = field(default_factory=int)
    estado: int = field(default_factory=int)
    imagen: list[str] = field(default_factory=list)
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    fecha_publicacion: str = field(default_factory=str)
    fecha_baja: str = field(default_factory=str)
    habitaciones: int = field(default_factory=int)
    baños: int = field(default_factory=int)
    estacionamientos: int = field(default_factory=int)
    superficie: int = field(default_factory=int)
