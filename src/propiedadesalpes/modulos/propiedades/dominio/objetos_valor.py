"""Objetos valor del dominio de cliente

En este archivo usted encontrará los objetos valor del dominio de cliente

"""

from seedwork.dominio.objetos_valor import ObjetoValor, Ciudad
from dataclasses import dataclass

@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombre: str

@dataclass(frozen=True)
class Email(ObjetoValor):
    address: str
    dominio: str
    es_empresarial: bool

@dataclass(frozen=True)
class Cedula(ObjetoValor):
    numero: int
    ciudad: Ciudad

@dataclass(frozen=True)
class Rut(ObjetoValor):
    numero: int
    ciudad: Ciudad

class MetodosPago(ObjetoValor):
    # TODO
    ...

@dataclass(frozen=True)
class Descripcion(ObjetoValor):
    descripcion: str

@dataclass(frozen=True)
class Direccion(ObjetoValor):
    calle: str
    numero: int
    ciudad: Ciudad
    region: str
    pais: str
    codigo_postal: str
