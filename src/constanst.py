from pathlib import Path

ROOT_DIR = Path().resolve().parent

#Ubicacion archivos CSV
CSVS_DIR = ROOT_DIR /'data'

# defino ruta para la ubicacion de mis archivos SQL
SQL_DIR = ROOT_DIR /'sql'


#Nombres de las tablas para Sql
TABLE_BASE = 'base'
CINE_INSIGHTS_TABLE = 'cine_insights_table'
CANT_FUENTE_TABLE= 'cant_fuente_table'
CANT_CATEGORIA_TABLE = 'cant_categoria_table'
CANT_PROV_CATEGORIA_TABLE = 'cant_categ_prov_table'


TABLES = [
    TABLE_BASE ,
    CINE_INSIGHTS_TABLE,
    CANT_FUENTE_TABLE,
    CANT_CATEGORIA_TABLE,
    CANT_PROV_CATEGORIA_TABLE
]

