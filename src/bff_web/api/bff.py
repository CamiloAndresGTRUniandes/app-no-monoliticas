import logging
import presentacion.api as api
from flask import Response
from flask import request
import requests


bp = api.crear_blueprint('propiedades', '/api/v1/propiedades')
url_propiedades = "http://127.0.0.1:5000/propiedad"
url_usuarios = "http://127.0.0.1:3000/user"
url_ventas = "http://127.0.0.1:7000/sales"
url_companias = "http://127.0.0.1:6000/company"

@bp.route('/crear', methods=('POST',))
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
        resp = requests.post(f"{url_propiedades}/crear", json= data)
        if (resp.status_code == 202):
            return {"estado":"Creación de propiedad en progreso..."}, 202
        else:
            return Response({"estado":f"Error en la creación de la propiedad: {data['nombre']}"}, status=400, mimetype='application/json')
    except Exception as e:
        logging.error(f"ERROR BFF: {e}")

@bp.route('', methods=('GET',))
def obtener_propiedades():
    try:
        resp = requests.get(f"{url_propiedades}")
        if (resp.status_code == 200):
            return {"estado":"Consulta de propiedades exitosa", "data": f"{resp.json()}"}, 200
        else:
            return Response({"estado":f"Error en la consulta de propiedades"}, status=400, mimetype='application/json')
    except Exception as e:
        logging.error(f"ERROR BFF: {e}")

@bp.route('/usuario/registrar', methods=('POST',))
def registrar_usuario():
    try:
        usuario = request.json
        data = {
            "firstName": usuario["firstName"],
            "lastName": usuario["lastName"],
            "userName": usuario["userName"],
            "password": usuario["password"]
        }
        resp = requests.post(f"{url_usuarios}", json= data)
        if (resp.status_code == 202):
            return {"estado":"registro de usuario en progreso..."}, 202
        else:
            return {"estado":f"Error en la creación del usuario: {data['nombre']}"}, 400
    except Exception as e:
        logging.error(f"ERROR BFF: {e}")

@bp.route('/usuario/login', methods=('POST',))
def login_usuario():
    try:
        usuario = request.json
        data = {
            "userName": usuario["userName"],
            "password": usuario["password"]
        }
        resp = requests.post(f"{url_usuarios}/login", json= data)
        if (resp.status_code == 200):
            response = resp.json()
            return {"estado":"Inicio de sesión exitoso", "token": f"{response['token']}"}, 200
        else:
            return {"estado":f"Error en el inicio de sesión, credenciales invalidas"}, 400
    except Exception as e:
        logging.error(f"ERROR BFF: {e}")

@bp.route('/ventas/crear', methods=('POST',))
def crear_venta():
    try:
        venta = request.json
        data = {
            "name": f"{venta['name']}",
            "price": venta['price'],
            "currency": f"{venta['currency']}",
            "property_id": f"{venta['property_id']}"
        }
        resp = requests.post(f"{url_ventas}", json= data)
        if (resp.status_code == 202):
            return {"estado":f"Creación de venta en progreso para la propiedad: {data['property_id']}"}, 202
        else:
            return {"estado":f"Error en la creación de la venta para la propiedad: {data['property_id']}"}, 400
    except Exception as e:
        logging.error(f"ERROR BFF: {e}")

@bp.route('/ventas', methods=('GET',))
def obtener_ventas():
    try:
        resp = requests.get(f"{url_ventas}")
        if (resp.status_code == 200):
            return {"estado":"Consulta de propiedades exitosa", "data": f"{resp.json()}"}, 200
        else:
            return Response({"estado":f"Error en la consulta de ventas"}, status=400, mimetype='application/json')
    except Exception as e:
        logging.error(f"ERROR BFF: {e}")

@bp.route('/company/crear', methods=('POST',))
def crear_compania():
    try:
        compania = request.json
        data = {
            "name": f"{compania['name']}",
            "nit": f"{compania['nit']}",
            "address": f"{compania['address']}",
            "city": f"{compania['city']}",
            "country": f"{compania['country']}",
            "property_id": f"{compania['property_id']}",
        }
        resp = requests.post(f"{url_companias}", json= data)
        if (resp.status_code == 202):
            return {"estado":f"Creación de compañia en progreso: {data['name']}"}, 202
        else:
            return {"estado":f"Error en la creación de la compañia: {data['name']}"}, 400
    except Exception as e:
        logging.error(f"ERROR BFF: {e}")

@bp.route('/company', methods=('GET',))
def obtener_companias():
    try:
        resp = requests.get(f"{url_companias}")
        print(f"companies response code: {resp.status_code}")
        if (resp.status_code == 200):
            return {"estado":"Consulta de compañias exitosa", "data": f"{resp.json()}"}, 200
        else:
            return Response({"estado":f"Error en la consulta de compañias"}, status=400, mimetype='application/json')
    except Exception as e:
        logging.error(f"ERROR BFF: {e}")