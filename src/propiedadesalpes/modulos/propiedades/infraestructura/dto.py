"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos

"""

from config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table, DECIMAL

import uuid

Base = db.declarative_base()

# Tabla intermedia para tener la relación de muchos a muchos entre la tabla reservas e itinerarios
class Propiedad(db.Model):
    __tablename__ = "propiedades"
    id = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String, nullable=True)
    precio = db.Column(db.DECIMAL, nullable=True)
    direccion = db.Column(db.String, nullable=True)
    tipo = db.Column(db.Integer, nullable=True)
    estado = db.Column(db.Integer, nullable=True)
    habitaciones = db.Column(db.Integer, nullable=True)
    banos = db.Column(db.Integer, nullable=True)
    precio = db.Column(db.Integer, nullable=True)
    imagen = db.Column(db.String, nullable=True)
    fecha_creacion = db.Column(db.DateTime, nullable=True)
    fecha_actualizacion = db.Column(db.DateTime, nullable=True)
    fecha_publicacion = db.Column(db.DateTime, nullable=True)
    fecha_baja = db.Column(db.DateTime, nullable=True)
    estacionamientos = db.Column(db.Integer, nullable=True)
    superficie = db.Column(db.Integer, nullable=True)

