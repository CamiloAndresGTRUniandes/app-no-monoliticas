import pulsar
from pulsar.schema import *
import pika

from modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreada, PropiedadCreadaPayload
from modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad, ComandoCrearPropiedadPayload
from seedwork.infraestructura import utils

import datetime
import json

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



    def _publicar_mensaje_rabbit(self, mensaje, topico):
        credentials = pika.PlainCredentials(username=f'{utils.broker_rabbit_user()}', password=f'{utils.broker_rabbit_password()}')
        connection = pika.BlockingConnection(pika.ConnectionParameters(f'{utils.broker_rabbit_host()}', port=utils.broker_rabbit_port(), credentials= credentials))
        channel = connection.channel()
        channel.exchange_declare(exchange=topico, exchange_type='topic', durable=True)
        message = mensaje
        
        channel.basic_publish(exchange=topico, routing_key=f'{utils.broker_rabbit_password()}', body=message)
        connection.close()

    def publicar_evento_rabbit(self, evento, topico):
        payload = {
            "id_propiedad" : f'{evento.id_propiedad}',
            "nombre" : f"{evento.nombre}",
            "estado" : f"{evento.estado}",
            "fecha_creacion" : f"{evento.fecha_creacion}",
            "fecha_actualizacion" : f"{evento.fecha_actualizacion}",
            "direccion" : f"{evento.direccion}",
            "tipo" : f"{evento.tipo}",
            "precio" : f"{evento.precio}",
            "imagen" : f"{evento.imagen}",
            "habitaciones" : f"{evento.habitaciones}",
            "banos" : f"{evento.banos}",
            "superficie" : f"{evento.superficie}",
            "estacionamientos" : f"{evento.estacionamientos}",
            "fecha_publicacion" : f"{evento.fecha_publicacion}",
            "fecha_baja" : f"{evento.fecha_baja}",
            "descripcion" : f"{evento.descripcion}"
            }
        mensaje = json.dumps(payload)
        self._publicar_mensaje_rabbit(mensaje, topico)
