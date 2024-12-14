from setuptools import setup, find_packages

setup(
    name="TestRelease",                                # Nombre del paquete
    version="0.1.0",                                   # Versión inicial
    packages=find_packages(),                          # Paquetes a incluir
    description="Un paquete pip simple de saludo",     # Breve descripción
    author="Josue Say",                                # Tu nombre
    author_email="josuesay770@gmail.com",              # Tu correo electrónico
    url="https://github.com/josuesay/TestRelease",     # URL del proyecto
)