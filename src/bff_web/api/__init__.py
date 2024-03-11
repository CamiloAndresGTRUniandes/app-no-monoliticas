import os
from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'

     # Importa Blueprints
    from . import bff
    # Registro de Blueprints
    app.register_blueprint(bff.bp)
    from flask_swagger import swagger
    @app.route("/api/v1//spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/api/v1/health")
    def health():
        return {"status": "up"}

    return app