from pathlib import Path

#Donde voy a poner mis archivos
BASE_FILE_DIR = Path('/tmp')

# Ubicacion de mi proyecto
# Resolve me da la ubicacion actual
# parent me da la carpeta madre de la carpeta actual
ROOT_DIR = Path().resolve().parent

#creo ruta para la ubicacion de mis archivos SQL
SQL_DIR = ROOT_DIR / 'challenge/sql'


#Nombres de las tablas para Sql

RAW_TABLE_NAME = 'raw'
CINE_INSIGHTS_TABLE_NAME = 'cine_insights'
SOURCE_SIZE_TABLE_NAME = 'size_by_datasource'
CATEGORY_COUNT_TABLE_NAME = 'size_by_category'
PROV_CAT_COUNT_TABLE_NAME = 'size_by_datasource'


TABLE_NAMES = [
    RAW_TABLE_NAME,
    CINE_INSIGHTS_TABLE_NAME,
    SOURCE_SIZE_TABLE_NAME,
    CATEGORY_COUNT_TABLE_NAME,
    PROV_CAT_COUNT_TABLE_NAME,
]