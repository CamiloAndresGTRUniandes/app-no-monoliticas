from config.db import db
from seedwork.aplicacion.servicios import Servicio
from modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from modulos.propiedades.infraestructura.dto import Propiedad as PropiedadDTOInf
from modulos.propiedades.dominio.fabricas import FabricaPropiedades
from modulos.propiedades.dominio.entidades import Propiedad
from modulos.propiedades.dominio.objetos_valor import Company
from modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from seedwork.infraestructura.unit_of_work_prop import UnidadTrabajoPuerto
from flask import Flask
from .dto import PropiedadDTO
from .mapeadores import MapeadorPropiedad
import os

class ServicioPropiedad(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio 
    
    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades
    
    def crear_propiedad(self, dto: PropiedadDTO) -> PropiedadDTO:
        propiedad : Propiedad = self._fabrica_propiedades.crear_objeto(dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.commit()

        return self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())
    
    def obtener_propiedad_por_id(self, id) -> PropiedadDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        return self._fabrica_propiedades.crear_objeto(repositorio.obtener_por_id(id), MapeadorPropiedad())
    
    def actualizar_propiedad_vendida(self, id):
        try:
            from modulos.propiedades.infraestructura.event_context import app
            with app.app_context():
                propiedad = db.session.query(PropiedadDTOInf).filter_by(id= id).one()
                propiedad.vendido = 1
                db.session.commit()
        except Exception as e:
            print(f"Error actualizando: {e}")

    def agregar_compania(self, id_propiedad, compania : Company):
        try:
            from modulos.propiedades.infraestructura.event_context import app
            with app.app_context():
                propiedad: Propiedad = db.session.query(PropiedadDTOInf).filter_by(id= id_propiedad).one()
                propiedad.agregar_compania(compania)
                db.session.commit()
        except Exception as e:
            print(f"Error actualizando: {e}")