import os
from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask import Flask

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def registrar_handlers():
    import src.propiedadesalpes.modulos.propiedades.aplicacion

def importar_modelos_alchemy():
    import src.propiedadesalpes.modulos.propiedades.infraestructura.dto


def comenzar_consumidor():
    """
    Este es un código de ejemplo. Aunque esto sea funcional puede ser un poco peligroso tener 
    threads corriendo por si solos. Mi sugerencia es en estos casos usar un verdadero manejador
    de procesos y threads como Celery.
    """

    import threading
    import src.propiedadesalpes.modulos.propiedades.infraestructura.consumidores as propiedad


    # Suscripción a eventos
    threading.Thread(target=propiedad.suscribirse_a_eventos).start()

    # Suscripción a comandos
    threading.Thread(target=propiedad.suscribirse_a_comandos).start()

def create_app():
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f"postgresql://postgres:postgres@127.0.0.1:5432/propiedades"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    #app.config['TESTING'] = configuracion.get('TESTING')

     # Inicializa la DB


    from src.propiedadesalpes.config.db import init_db
    init_db(app)

    from src.propiedadesalpes.config.db import db

    importar_modelos_alchemy()
    registrar_handlers()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            comenzar_consumidor()

     # Importa Blueprints
    from . import propiedad
    # Registro de Blueprints
    app.register_blueprint(propiedad.bp)
    from flask_swagger import swagger
    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
