import datetime
import json
import time
from modulos.propiedades.aplicacion.comandos.actualizar_propiedad_vendida import ActualizarPropiedadVendida
from modulos.propiedades.aplicacion.servicios import ServicioPropiedad
from modulos.propiedades.dominio.objetos_valor import Company
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from modulos.propiedades.aplicacion.comandos.crear_cache_propiedad import CrearCachePropiedad
from modulos.propiedades.infraestructura.schema.v1.eventos import CompanyCreatedEvent, EventoPropiedadCreada, PropertySoldEvent
from modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad
from seedwork.aplicacion.comandos import ejecutar_commando
from seedwork.infraestructura import utils


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-propiedad', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadesalpes-sub-eventos', schema=AvroSchema(EventoPropiedadCreada))

        while True:
            mensaje = consumidor.receive()
            ex = mensaje.value()
            propiedad_dto = ex.data
            comando = CrearCachePropiedad(
                id_propiedad= propiedad_dto.id_propiedad,
                nombre= propiedad_dto.nombre,
                descripcion= propiedad_dto.descripcion,
                direccion= propiedad_dto.direccion,
                precio= propiedad_dto.precio,
                fecha_creacion= propiedad_dto.fecha_creacion,
                fecha_actualizacion= propiedad_dto.fecha_actualizacion,
                fecha_publicacion= propiedad_dto.fecha_publicacion,
                fecha_baja= propiedad_dto.fecha_baja,
                estado= propiedad_dto.estado,
                tipo= propiedad_dto.tipo,
                habitaciones= propiedad_dto.habitaciones,
                banos= propiedad_dto.banos,
                estacionamientos=  propiedad_dto.estacionamientos,
                superficie= propiedad_dto.superficie,
                imagen= propiedad_dto.imagen,
                vendido= propiedad_dto.vendido
                )
            ejecutar_commando(comando)
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_eventos_ventas():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('sales-property', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='sales-sub-eventos', schema=AvroSchema(PropertySoldEvent))

        while True:
            
            mensaje = consumidor.receive()
            ex = mensaje.value()
            message = ex.data
            print(f"PopertySold Recieved XXX: {message}")
            if (message.property_id):
                sp = ServicioPropiedad()
                sp.actualizar_propiedad_vendida(message.property_id)

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()  

def suscribirse_a_eventos_companias():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('company-events', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='company-sub-eventos', schema=AvroSchema(CompanyCreatedEvent))

        while True:
            
            mensaje = consumidor.receive()
            ex = mensaje.value()
            message = ex.data
            print(f"PopertySold Recieved XXX: {message}")
            if (message.property_id):
                sp = ServicioPropiedad()
                sp.agregar_compania(Company(
                    id = message.id,
                    name = message.name,
                    nit = message.nit,
                    address = message.address,
                    city = message.city,
                    country = message.country,
                    created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    ))

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()  

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-propiedad', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propiedadesalpes-sub-comandos', schema=AvroSchema(ComandoCrearPropiedad))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.data()}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

import pika
def suscribirse_a_eventos_rabbit():
    def callback(ch, method, properties, body):
            propiedad_dto = json.loads(body)
            comando = CrearCachePropiedad(
                id_propiedad= propiedad_dto['id_propiedad'],
                nombre= propiedad_dto['nombre'],
                descripcion= propiedad_dto['descripcion'],
                direccion= propiedad_dto['direccion'],
                precio= propiedad_dto['precio'],
                fecha_creacion= propiedad_dto['fecha_creacion'],
                fecha_actualizacion= propiedad_dto['fecha_actualizacion'],
                fecha_publicacion= propiedad_dto['fecha_publicacion'],
                fecha_baja= propiedad_dto['fecha_baja'],
                estado= propiedad_dto['estado'],
                tipo= propiedad_dto['tipo'],
                habitaciones= propiedad_dto['habitaciones'],
                banos= propiedad_dto['banos'],
                estacionamientos=  propiedad_dto['estacionamientos'],
                superficie= propiedad_dto['superficie'],
                imagen= propiedad_dto['imagen'],
                vendido = propiedad_dto['vendido'])
            ejecutar_commando(comando)
    topico = 'comandos-propiedad'
    connection = conectar_rabbitmq()
    channel = connection.channel()
    channel.exchange_declare(exchange=topico, exchange_type='topic', durable=True)
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange=topico, queue=queue_name, routing_key=f'{utils.broker_rabbit_password()}')
    print(f" [*] Esperando mensajes en el topico {topico}. Para salir, presiona Ctrl+C")
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


def conectar_rabbitmq(intentos_maximos=5, intervalo_reintentos_segundos=5):
    intentos = 0
    while intentos < intentos_maximos:
        try:
            credentials = pika.PlainCredentials(username=f'{utils.broker_rabbit_user()}', password=f'{utils.broker_rabbit_password()}')
            connection = pika.BlockingConnection(pika.ConnectionParameters(f'{utils.broker_rabbit_host()}', port=utils.broker_rabbit_port(), credentials= credentials))
            logging.warning('SUCCESS: Conexion exitosa a RabbitMQ!')
            return connection
        except pika.exceptions.AMQPConnectionError:
            logging.warning("No se pudo establecer la conexión. Reintentando...")
            intentos += 1
            time.sleep(intervalo_reintentos_segundos)

    logging.error('ERROR: Conexión a rabbit no exitosa despues de reintentos')
    return None
    