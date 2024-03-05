from pulsar.schema import *
from seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PropiedadCreadaPayload(Record):
    id_propiedad = String()
    nombre = String()
    estado = String()
    fecha_creacion = String()
    fecha_actualizacion = String()
    direccion = String()
    tipo = String()
    precio = String()
    imagen = String()
    habitaciones = String()
    banos = String()
    superficie = String()
    estacionamientos = String()
    fecha_publicacion = String()
    fecha_baja = String()
    descripcion = String()


class EventoPropiedadCreada(EventoIntegracion):
    data = PropiedadCreadaPayload()