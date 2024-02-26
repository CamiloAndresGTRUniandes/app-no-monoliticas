import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from modulos.propiedades.aplicacion.comandos.crear_cache_propiedad import CrearCachePropiedad

from modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreada
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
                imagen= propiedad_dto.imagen
                )
            ejecutar_commando(comando)
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