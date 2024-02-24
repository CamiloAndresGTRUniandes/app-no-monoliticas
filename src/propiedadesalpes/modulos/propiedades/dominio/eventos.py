from __future__ import annotations
import array
from dataclasses import dataclass
import uuid
from propiedadesalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class PropiedadCreada(EventoDominio):
    id_propiedad: uuid.UUID = None
    nombre: str = None
    descripcion: str = None
    estado: str = None
    tipo: str = None
    direccion: str = None
    precio: float = None
    habitaciones: int = None
    baños: int = None
    estacionamientos: int = None
    superficie: int = None
    imagen: array = None
    fecha_creacion: datetime = None
    fecha_actualizacion: datetime = None
    fecha_publicacion: datetime = None
    fecha_baja: datetime = None
