

import pytest
from src.propiedadesalpes.modulos.propiedades.dominio.fabricas import FabricaPropiedades


"""
    Clases de Soporte para validar el seedwork
"""

class FabricaImplementada(FabricaPropiedades):
    def crear_objeto(self, obj: any, mapeador: any) -> any:
        return "Mi Objeto"

class FabricaSinImplementar(FabricaPropiedades):
    ...

"""
    Pruebas
"""

def test_crear_fabrica_sin_implementacion():
    with pytest.raises(TypeError):
        fabrica = FabricaSinImplementar()

def test_crear_fabrica_con_implementacion():
    # Dada un nueva fabrica
    fabrica = FabricaImplementada()

    # Con metodo creacional
    assert fabrica.crear_objeto({}, {}) is not None
