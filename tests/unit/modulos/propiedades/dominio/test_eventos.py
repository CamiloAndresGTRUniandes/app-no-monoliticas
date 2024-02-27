import pytest
from datetime import datetime
import uuid
from src.propiedadesalpes.modulos.propiedades.dominio.eventos import PropiedadCreada


def crear_propiedad():
    return PropiedadCreada(
        id_propiedad=uuid.UUID('123e4567-e89b-12d3-a456-426614174000'),
        nombre="Nombre de la propiedad",
        descripcion="Descripción de la propiedad con 'comillas simples'",
        estado="Activo",
        tipo="Casa",
        direccion="Dirección de la propiedad",
        precio=100000.0,
        habitaciones=3,
        banos=2,
        estacionamientos=1,
        superficie=150,
        imagen="imagen.jpg",
        fecha_creacion=datetime.now(),
        fecha_actualizacion=datetime.now(),
        fecha_publicacion=datetime.now(),
        fecha_baja=None
    )

def test_propiedad_creada():
    propiedades=crear_propiedad()
    assert propiedades.nombre == "Nombre de la propiedad"
    assert propiedades.estado == "Activo"
    assert propiedades.superficie == 150