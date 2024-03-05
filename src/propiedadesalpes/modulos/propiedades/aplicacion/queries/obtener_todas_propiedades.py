from dataclasses import dataclass
from seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from seedwork.aplicacion.queries import ejecutar_query as query
from modulos.propiedades.dominio.entidades import Propiedad
from modulos.propiedades.aplicacion.dto import PropiedadDTO
from .base import ReservaQueryBaseHandler


@dataclass
class ObtenerTodasPropiedades(Query):
    ...

class ObtenerTodasPropiedadesHandler(ReservaQueryBaseHandler):

    FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def handle(self, query) -> QueryResultado:
        propiedades_dto = []
        vista = self.fabrica_vista.crear_objeto(Propiedad)
        propiedades = vista.obtener_todos()

        for propiedad in propiedades:
            dto = PropiedadDTO(
                fecha_creacion=propiedad.fecha_creacion,
                fecha_actualizacion=propiedad.fecha_actualizacion,
                id_propiedad = propiedad.id,
                nombre = propiedad.nombre,
                descripcion = propiedad.descripcion,
                precio = propiedad.precio,
                fecha_publicacion = propiedad.fecha_publicacion,
                fecha_baja= propiedad.fecha_baja,
                estado= propiedad.estado,
                tipo= propiedad.tipo,
                habitaciones= propiedad.habitaciones,
                banos= propiedad.banos,
                estacionamientos= propiedad.estacionamientos,
                superficie= propiedad.superficie,
                imagen= propiedad.imagen,
                direccion=propiedad.direccion)
            propiedades_dto.append(dto)
        
        return QueryResultado(resultado=propiedades_dto)

@query.register(ObtenerTodasPropiedades)
def ejecutar_query_obtener_propiedad(query: ObtenerTodasPropiedades):
    handler = ObtenerTodasPropiedadesHandler()
    return handler.handle(query)