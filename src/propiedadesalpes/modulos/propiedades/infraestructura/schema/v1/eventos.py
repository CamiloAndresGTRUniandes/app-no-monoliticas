from pulsar.schema import *
from src.propiedadesalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PropiedadCreadaPayload(Record):
    id_propiedad = String()
    nombre = String()
    estado = String()
    fecha_creacion = Long()
    fecha_actualizacion = Long()
    direccion = String()
    tipo = String()
    precio = Double()
    imagen = String()
    habitaciones = Integer()
    banos = Integer()
    superficie = Integer()
    estacionamientos = Integer()
    fecha_publicacion = Long()
    fecha_baja = Long()
    descripcion = String()


class EventoPropiedadCreada(EventoIntegracion):
    data = PropiedadCreadaPayload()