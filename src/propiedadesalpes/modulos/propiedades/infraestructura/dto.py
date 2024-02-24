"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos

"""

from src.propiedadesalpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

# Tabla intermedia para tener la relación de muchos a muchos entre la tabla reservas e itinerarios
class Propiedad(db.Model):
    __tablename__ = "propiedades"
    id = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String, nullable=False)
    ubicacion = db.Column(db.String, nullable=False)
    tipo = db.Column(db.String, nullable=False)
    habitaciones = db.Column(db.Integer, nullable=False)
    baños = db.Column(db.Integer, nullable=False)
    camas = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    imagen = db.Column(db.String, nullable=False)

