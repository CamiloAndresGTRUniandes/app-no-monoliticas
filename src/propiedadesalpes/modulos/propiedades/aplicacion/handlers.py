

from modulos.propiedades.dominio.eventos import PropiedadCreada
from seedwork_prop.aplicacion.handlers import Handler
from modulos.propiedades.infraestructura.despachadores import Despachador

class HandlerPropiedadDominio(Handler):

    @staticmethod
    def handle_propiedad_creada(evento):
        try:
            despachador = Despachador()
            despachador.publicar_comando_rabbit(evento, 'comandos-propiedad')
        except Exception as e:
            print(f"ERROR AL PUBLICAR {e}")
        