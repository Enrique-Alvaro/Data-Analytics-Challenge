from sqlalchemy import create_engine
from sqlalchemy.sql import text
from constanst import SQL_DIR,TABLE_NAMES
from cfg import DB_CONNSTR
import logging

#conexion para la DB, el parametro es la direccion con la cual nos vamos a conectar a la db
engine = create_engine(DB_CONNSTR)

log = logging.getLogger()

def create_tables():
    ''''Creo las tablas de la db'''
    with engine.connect() as con:
        for file in TABLE_NAMES:
            log.info(f'Creando tabla {file}')
            with open (SQL_DIR/f'{file}.sql') as f:
                query = text(f.read())

            con.execute(f'DROP TABLE IF EXISTS {file}')
            con.execute(query)



if __name__ == '__main__':
    create_tables()
