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
        print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{propiedad_dict}')
        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)

        sp = ServicioPropiedad()
        dto_final = sp.crear_propiedad(propiedad_dto)

        return map_propiedad.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')