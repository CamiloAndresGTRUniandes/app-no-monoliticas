
from config.db import db
from sqlalchemy import ForeignKey

Base = db.declarative_base()

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
    vendido = db.Column(db.Integer, nullable=True)
    companies = db.relationship('companies', secondary = 'property_company')

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=True)
    nit = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=True)
    country = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=True)
    properties = db.relationship('properties', secondary = 'property_company')


class PropertyCompany(db.Model):
    __tablename__ = "property_company"
    property_id = db.Column(db.String, ForeignKey('propiedades.id'), primary_key=True)
    company_id = db.Column(db.String, ForeignKey('companies.id'), primary_key=True)