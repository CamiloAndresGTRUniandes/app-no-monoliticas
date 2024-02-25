import pulsar
from pulsar.schema import *

from src.propiedadesalpes.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreada, PropiedadCreadaPayload
from src.propiedadesalpes.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad, ComandoCrearPropiedadPayload
from src.propiedadesalpes.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoPropiedadCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = PropiedadCreadaPayload(
            id_propiedad = evento.id_propiedad,
            nombre = evento.nombre,
            estado = evento.estado,
            fecha_creacion = evento.fecha_creacion,
            fecha_actualizacion = evento.fecha_actualizacion,
            direccion = evento.direccion,
            tipo = evento.tipo,
            precio = evento.precio,
            imagen = evento.imagen,
            habitaciones = evento.habitaciones,
            banos = evento.banos,
            superficie = evento.superficie,
            estacionamientos = evento.estacionamientos,
            fecha_publicacion = evento.fecha_publicacion,
            fecha_baja = evento.fecha_baja,
            descripcion = evento.descripcion)
        
        evento_integracion = EventoPropiedadCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoPropiedadCreada))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearPropiedadPayload(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearPropiedad(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearPropiedad))
