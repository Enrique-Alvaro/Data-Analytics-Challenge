from sqlalchemy import create_engine
from cfg import URL_DB
import pandas as pd
from constanst import (
    TABLE_BASE ,
    CINE_INSIGHTS_TABLE,
    CANT_FUENTE_TABLE,
    CANT_CATEGORIA_TABLE,
    CANT_PROV_CATEGORIA_TABLE
)
import logging
from sqlalchemy_utils import database_exists, create_database

def conect_db():
    ''''Me conecto a la db'''
    log.info(f'Conexion a la DB')
    if not database_exists(URL_DB):
        log.info(f'Creo la DB')
        create_database(URL_DB)
    
    engine = create_engine(URL_DB)

    return engine


class BaseLoader():
    table_name = TABLE_BASE

    def load_table(self, file_path):
        df = pd.read_csv(file_path,encoding='latin-1')
        df.to_sql(TABLE_BASE, con= engine, index = False, if_exists = 'replace')

class CineInsightsLoader():
    table_name = CINE_INSIGHTS_TABLE

    def load_table(self, file_path):
        df = pd.read_csv(file_path,encoding='latin-1')

        insights_df = df.groupby('Provincia', as_index= False).count()[
            {'Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA'}
        ]
    
        insights_df.to_sql(CINE_INSIGHTS_TABLE, con= engine, index = False, if_exists = 'replace')


class CantCategoriaLoader():
    table_name = CANT_CATEGORIA_TABLE

    def load_table(self, file_path):
        df = pd.read_csv(file_path,encoding='latin-1')
        categoria_df = df.groupby(['categoria'], as_index=False).size()

        categoria_df.to_sql(CANT_CATEGORIA_TABLE, con= engine, index = False, if_exists = 'replace')


class CantFuenteLoader():
    table_name = CANT_FUENTE_TABLE

    def load_table(self, file_path):
        lst = list()

        for name, file_path in file_path.items():
            df = pd.read_csv(file_path,encoding='latin-1')
            lst.append({'source': name, 'count':df.size})
        
        df_fuente = pd.DataFrame(lst)
        df_fuente.to_sql(CANT_FUENTE_TABLE, con= engine, index = False, if_exists = 'replace')



class CantProvCategoria():
    table_name = CANT_PROV_CATEGORIA_TABLE

    def load_table(self, file_path):
        df = pd.read_csv(file_path,encoding='latin-1')
        df_prov_categoria = df.groupby(['categoria', 'provincia'], as_index=False).size()

        df_prov_categoria.to_sql(CANT_PROV_CATEGORIA_TABLE, con= engine, index = False, if_exists = 'replace')
    


if __name__ == "__main__":
    log = logging.getLogger()

    engine  = conect_db()