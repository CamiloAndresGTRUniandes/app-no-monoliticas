
from company.modules.company.application.commands.create_company import CreateCompany
from company.modules.company.domain.events import CompanyCreated
from modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
from modulos.propiedades.dominio.eventos import CreacionPropiedadFallida, PropiedadCreada
from modulos.propiedades.infraestructura.repositorios import RepositorioSagaLog
from modulos.sagas.aplicacion.commandos.sales import CreateSaleFailed
from modulos.sagas.aplicacion.commandos.company import CreateCompanyFailed
from sales.modules.sales.domain.events import PropertySold, SaleCreated
from seedwork.aplicacion.sagas import *


class CoordinadorPropiedades(CoordinadorOrquestacion):
    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearPropiedad, evento=PropiedadCreada, error=CreacionPropiedadFallida, compensacion=None),
            Transaccion(index=2, comando=SaleCreated, evento=PropertySold, error=CreateSaleFailed, compensacion=None),
            Transaccion(index=3, comando=CreateCompany, evento=CompanyCreated, error=CreateCompanyFailed, compensacion=None),
            Fin(index=4)
        ]
    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])

    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])


    def persistir_en_saga_log(self, mensaje):
        repositorio = RepositorioSagaLog()
        repositorio.agregar(mensaje)
