

from propiedadesalpes.modulos.propiedades.dominio.eventos import PropiedadCreada
from propiedadesalpes.seedwork.aplicacion.handlers import Handler

class HandlerPropiedadDominio(Handler):

    @staticmethod
    def handle_propiedad_creada(evento):
        print('================ PROPIEDAD CREADA ===========')
        

    