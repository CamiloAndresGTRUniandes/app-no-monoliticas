import threading
import subprocess

def ejecutar_comando_clients():
    comando = "flask --app src/clientes/api run --debugger --no-reload -p 3000"
    subprocess.call(comando, shell=True)

def ejecutar_comando_properties():
    comando = "flask --app src/propiedadesalpes/api run --debugger --no-reload -p 5000"
    subprocess.call(comando, shell=True)

def ejecutar_comando_companies():
    comando = "flask --app src/company/api run --debugger --no-reload -p 6000"
    subprocess.call(comando, shell=True)

# Crear un hilo para ejecutar el comando
thread_cliente = threading.Thread(target=ejecutar_comando_clients)
thread_cliente.start()

thread_propiedades = threading.Thread(target=ejecutar_comando_properties)
thread_propiedades.start()

thread_comapnies = threading.Thread(target=ejecutar_comando_companies)
thread_comapnies.start()


