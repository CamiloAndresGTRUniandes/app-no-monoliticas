import src.propiedadesalpes.seedwork.presentacion.api as api
from src.propiedadesalpes.seedwork.dominio.excepciones import ExcepcionDominio
from src.propiedadesalpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from src.propiedadesalpes.modulos.propiedades.aplicacion.servicios import ServicioPropiedad
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

        sp = ServicioPropiedad()
        dto_final = sp.crear_propiedad(propiedad_dto)

        return map_propiedad.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('/<id>', methods=('GET',))
def dar_propiedad(id=None):
    if id:
        sr = ServicioPropiedad()
        map_propiedad = MapeadorPropiedadDTOJson()
        
        return map_propiedad.dto_a_externo(sr.obtener_propiedad_por_id(id))
    else:
        return [{'message': 'GET!'}]