import seedwork.presentacion.api as api
from seedwork.dominio.excepciones import ExcepcionDominio
from modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
from modulos.propiedades.aplicacion.queries.obtener_todas_propiedades import ObtenerTodasPropiedades
from seedwork.aplicacion.queries import ejecutar_query
from seedwork.aplicacion.comandos import ejecutar_commando
import json
from flask import Response
from flask import redirect, render_template, request, session, url_for


bp = api.crear_blueprint('propiedad', '/propiedad')

@bp.route('/crear', methods=['POST',])
def crear():
    try:
        propiedad_dict = request.json
        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)

        comando = CrearPropiedad(
            nombre=propiedad_dto.nombre,
            descripcion=propiedad_dto.descripcion,
            direccion=propiedad_dto.direccion,
            precio=propiedad_dto.precio,
            fecha_creacion=propiedad_dto.fecha_creacion,
            fecha_actualizacion=propiedad_dto.fecha_actualizacion,
            fecha_publicacion=propiedad_dto.fecha_publicacion,
            fecha_baja=propiedad_dto.fecha_baja,
            estado=propiedad_dto.estado,
            tipo=propiedad_dto.tipo,
            habitaciones=propiedad_dto.habitaciones,
            banos=propiedad_dto.banos,
            estacionamientos=propiedad_dto.estacionamientos,
            superficie=propiedad_dto.superficie,
            imagen=propiedad_dto.imagen)

        ejecutar_commando(comando)
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('', methods=('GET',))
def dar_reserva_usando_query():
    map_propiedad = MapeadorPropiedadDTOJson()
    query_resultado = ejecutar_query(ObtenerTodasPropiedades())
    resultados = []
    
    for propiedad in query_resultado.resultado:
        resultados.append(map_propiedad.dto_a_externo(propiedad))
    
    return resultados
    