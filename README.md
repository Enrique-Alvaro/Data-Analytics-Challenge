# Challenge Data Analytics - Python 

## Objetivo
* Consumir datos de tres fuentes distintas
* Normalizar datos
* Cargar diferentes tablas propuestas

## Requisitos

### Poetry
Poetry es una herramienta que se encarga de la gestión de las dependencias y los paquetes en Python, es también capaz de crear entornos virtuales, aislando así las dependencias entre proyectos y centralizando todo lo relacionado con la gestión de paquetes en una única herramienta.
Para poder instalarlo se debe ejecutar `pip install poetry` , luego usando `poetry install`, creará un virtual env con todas las dependencias necesarias, luego puede acceder se debe ejecutar `poetry shell`.

Todas las dependencias pueden ser instalados desde el archivo `./requirements.txt`

### Conexion Base de datos
Paral la base de datos se utilizo postgres desde docker.

### Variables
Ademas se necesita un archivo settings.ini donde se le tiene que asignar valores a las siguientes variables 

`URL_DB, MUSEO_URL, CINES_URL, BIBLIOTECAS_URL`

## Ejecución
Para la creacion de la Base de Datos y sus respectivas tabalas se tiene ejecutar :
* `python script.py`

Luego para generar los csv y extraer/transformar/cargar los datos en las tablas se debe ejecutar el siguiente comando:
* `python challenge/main.py --date 2022-04-26`
