

from src.propiedadesalpes.modulos.propiedades.dominio.eventos import PropiedadCreada
from src.propiedadesalpes.seedwork.aplicacion.handlers import Handler
from src.propiedadesalpes.modulos.propiedades.infraestructura.despachadores import Despachador

class HandlerPropiedadDominio(Handler):

    @staticmethod
    def handle_propiedad_creada(evento):
        try:
            Despachador.publicar_evento(Despachador(),evento, 'eventos-propiedad')
        except Exception as e:
            print(f"ERROR AL PUBLICAR {e}")
        

    