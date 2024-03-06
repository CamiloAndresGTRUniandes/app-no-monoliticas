from seedwork.infraestructura.vistas import Vista
from modulos.propiedades.infraestructura.redis import RedisRepositorio
from modulos.propiedades.dominio.entidades import Propiedad
from config.db import db
from .dto import Propiedad as PropiedadDTO
import json



class VistaPropiedad(Vista):
    def obtener_todos(self):
        propiedades = list()
        redis = RedisRepositorio()
        propiedadesRedis = redis.lrange('propiedades', 0, -1)
        for propiedad_dto in propiedadesRedis:
            fixed = propiedad_dto.decode('utf-8')
            fixed = fixed.replace("'", '"')
            propiedad_dto = json.loads(fixed)

            propiedades.append(PropiedadDTO(id=propiedad_dto['id_propiedad'],
                                         nombre= propiedad_dto['nombre'],
                                         descripcion= propiedad_dto['descripcion'],
                                         direccion= propiedad_dto['direccion'],
                                         precio= propiedad_dto['precio'],
                                         fecha_creacion= propiedad_dto['fecha_creacion'],
                                         fecha_actualizacion= propiedad_dto['fecha_actualizacion'],
                                         fecha_publicacion = propiedad_dto['fecha_publicacion'],
                                         fecha_baja= propiedad_dto['fecha_baja'],
                                         estado= propiedad_dto['estado'],
                                         tipo= propiedad_dto['tipo'],
                                         habitaciones= propiedad_dto['habitaciones'],
                                         banos= propiedad_dto['banos'],
                                         estacionamientos= propiedad_dto['estacionamientos'],
                                         superficie= propiedad_dto['superficie'],
                                         imagen= propiedad_dto['imagen'],
                                         vendido = propiedad_dto['vendido']
                                        ))

        return propiedades
    
    def obtener_por(self, id=None, estado=None, id_cliente=None, **kwargs) -> [PropiedadDTO]:
        params = dict()
        if id:
            params['id'] = str(id)

        return db.session.query(PropiedadDTO).filter_by(**params)
