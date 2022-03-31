from pathlib import Path

BASE_FILE_DIR = Path('/tmp')

# Resolve me da la ubicacion actual
# parent me da la carpeta madre de la carpeta actual
ROOT_DIR = Path().resolve().parent
#creo ruta para el SQL
SQL_DIR = ROOT_DIR / 'challenge/sql'



RAW_TABLE_NAME = 'raw'
CINE_INSIGHTS_TABLE_NAME = 'cine_insights'
SOURCE_SIZE_TABLE_NAME = 'size_by_datasource'
CATEGORY_COUNT_TABLE_NAME = 'size_by_category'
