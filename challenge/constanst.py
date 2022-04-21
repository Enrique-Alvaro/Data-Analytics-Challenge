from pathlib import Path

#Ubicacion archivos CSV
CSVS_DIR = Path('/tmp')

ROOT_DIR = Path().resolve().parent

# defino ruta para la ubicacion de mis archivos SQL
SQL_DIR = ROOT_DIR /'challenge/sql'


#Nombres de las tablas para Sql
TABLE_BASE = 'base'
CINE_INSIGHTS_TABLE = 'cine_insights'
CANT_FUENTE_TABLE= 'cant_by_fuente'
CANT_CATEGORIA_TABLE = 'cant_by_categoria'
CANT_PROV_CATEGORIA_TABLE = 'cant_by_prov_categoria'


TABLES = [
    TABLE_BASE ,
    CINE_INSIGHTS_TABLE,
    CANT_FUENTE_TABLE,
    CANT_CATEGORIA_TABLE,
    CANT_PROV_CATEGORIA_TABLE
]

