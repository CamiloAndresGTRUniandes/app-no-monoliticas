import logging
import presentacion.api as api
from flask import Response
from flask import request
import requests


bp = api.crear_blueprint('propiedades', '/api/v1/propiedades')
url_propiedades = "http://127.0.0.1:5000/propiedad"

@bp.route('', methods=('POST',))
def crear_nueva_propiedad():
    try:
        propiedad = request.json
        data = {
            "nombre": propiedad['nombre'],
            "descripcion": propiedad['descripcion'],
            "direccion": propiedad['direccion'],
            "precio": propiedad['precio'],
            "estado": propiedad['estado'],
            "imagen": propiedad['imagen'],
            "habitaciones": propiedad['habitaciones'],
            "banos": propiedad['banos'],
            "vendido": propiedad['vendido']
        }
        resp = requests.post(url_propiedades, data = data)
        if (resp.status_code == 202):
            return Response({"estado":"Creación de propiedad en progreso..."}, status=202, mimetype='application/json')
        else:
            return Response({"estado":f"Error en la creación de la propiedad: {data['nombre']}"}, status=202, mimetype='application/json')
    except Exception as e:
        logging.error(f"ERROR BFF: {e}")