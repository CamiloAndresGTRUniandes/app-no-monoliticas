
from dataclasses import dataclass, field
from datetime import datetime

from seedwork.aplicacion.comandos import Comando
from modulos.propiedades.aplicacion.dto import PropiedadDTO
from modulos.propiedades.dominio.entidades import Propiedad
from modulos.propiedades.aplicacion.comandos.base import CrearPropiedadBaseHandler
from modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from seedwork.aplicacion.comandos import ejecutar_commando as comando
from modulos.propiedades.infraestructura.redis import RedisRepositorio

@dataclass
class CrearCachePropiedad(Comando):
    id_propiedad : str = field(default_factory=str)
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
    imagen: str = field(default_factory=str)

class CrearCachePropiedadHandler(CrearPropiedadBaseHandler):
    def handle(self, comando: CrearCachePropiedad):
        propiedad_dto = PropiedadDTO(
            id_propiedad= comando.id_propiedad,
            nombre=comando.nombre,
            descripcion=comando.descripcion,
            direccion=comando.direccion,
            precio=comando.precio,
            fecha_creacion=comando.fecha_creacion,
            fecha_actualizacion=comando.fecha_actualizacion,
            fecha_publicacion=comando.fecha_publicacion,
            fecha_baja=comando.fecha_baja,
            estado=comando.estado,
            tipo=comando.tipo,
            habitaciones=comando.habitaciones,
            banos=comando.banos,
            estacionamientos=comando.estacionamientos,
            superficie=comando.superficie,
            imagen=comando.imagen)
        
        # propiedad : Propiedad = self._fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        # propiedad.crear_propiedad(propiedad)

        # map_propiedad = MapeadorPropiedad()
        # propiedad_ext = map_propiedad.entidad_a_externo(propiedad)
        # print(f"PROPIEDAD QUE SE ENVIA A JSON {str(propiedad_ext)}")
        propiedad_ext = {
            "id_propiedad": comando.id_propiedad,
            "nombre": comando.nombre,
            "descripcion": comando.descripcion,
            "direccion": comando.direccion,
            "precio": comando.precio,
            "fecha_creacion": comando.fecha_creacion,
            "fecha_actualizacion": comando.fecha_actualizacion,
            "fecha_publicacion": comando.fecha_publicacion,
            "fecha_baja": comando.fecha_baja,
            "estado": comando.estado,
            "tipo": comando.tipo,
            "habitaciones": comando.habitaciones,
            "banos": comando.banos,
            "estacionamientos": comando.estacionamientos,
            "superficie": comando.superficie,
            "imagen": comando.imagen
        }
        redis = RedisRepositorio()
        redis.lpush("propiedades", str(propiedad_ext))

@comando.register(CrearCachePropiedad)
def ejecutar_comando_crear_reserva_cache(comando: CrearCachePropiedad):
    handler = CrearCachePropiedadHandler()
    handler.handle(comando)