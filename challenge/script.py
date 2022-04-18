from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.sql import text
from constanst import SQL_DIR,TABLE_NAMES
from cfg import URL_DB
import logging

log = logging.getLogger()



def conect_db():

    log.info(f'Conexion a la DB')
    if not database_exists(URL_DB):
        create_database(URL_DB)
    
    engine = create_engine(URL_DB)

    return engine



def create_tables(engine):
    ''''Creo las tablas de la db'''
    with engine.connect() as con:
        for file in TABLE_NAMES:
            log.info(f'Creando tabla {file}')
            with open (SQL_DIR/f'{file}.sql') as f:
                query = text(f.read())

            con.execute(f'DROP TABLE IF EXISTS {file}')
            con.execute(query)



if __name__ == '__main__':
    engine = conect_db()
    create_tables(engine)
