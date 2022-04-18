from http.client import ImproperConnectionState
from unicodedata import category, name
from constanst import BASE_FILE_DIR
from datetime import datetime
import requests 
import logging
import pandas as pd

log = logging.getLogger()

class UrlExtractor:
    file_path_crib =(
        '{category}/{year}-{month:02d}/{category}-{day:02d}-{month:02d}-{year}.csv'
    )

    def __init__(self, name, url) -> None:
        self.name = name
        self.url = url

    def extract(self, date_str) -> str:
        
        log.info(f'Extrayendo {self.name}')
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        file_path = self.file_path_crib.format(
            category=self.name, year = date.year, month = date.month, day = date.day
        )
        m_path = BASE_FILE_DIR / file_path
        m_path.parent.mkdir(parents=True, exist_ok= True)

        r = requests.get(self.url)
        r.encoding = 'utf-8'

        log.info(f'Storing file {m_path}')
        with open(m_path, 'w', encoding="utf-8") as f_out:
            f_out.write(r.text)

        return m_path

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:

        rename_columns = {
            'Cod_Loc' : 'cod_localidad',
            'IdProvincia' : 'id_provincia',
            'IdDepartamento' : 'id_departamento',
            'Provincia' : 'provincia',
            'Categoría' : 'categoria',
            'Dirección' : 'domicilio',
            'CP' : 'codigo postal',
            'Localidad' : 'localidad',
            'Nombre' : 'nombre',
            'Domicilio' : 'domicilio',
            'Teléfono' : 'numero de telefono',
            'Mail' : 'mail',
            'Web' : 'web'
        }

        df = df.rename(columns= rename_columns)

        column_list = [
            'cod_localidad',
            'id_provincia',
            'id_departamento',
            'categoria',
            'provincia',
            'localidad',
            'nombre',
            'domicilio',
            'codigo postal',
            'numero de telefono',
            'mail',
            'web'
        ]

        return df[column_list]

class MuseoExtractor(UrlExtractor):
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:

        rename_columns = {
            'Cod_Loc' : 'cod_localidad',
            'IdProvincia' : 'id_provincia',
            'IdDepartamento' : 'id_departamento',
            'direccion' : 'domicilio',
            'CP' : 'codigo postal',
            'telefono' : 'numero de telefono',
            'Mail' : 'mail',
            'Web' : 'web',
            'fuente' : 'Fuente'
        }  


        df = df.rename(columns= rename_columns)

        column_list = [
            'cod_localidad',
            'id_provincia',
            'id_departamento',
            'categoria',
            'provincia',
            'localidad',
            'nombre',
            'domicilio',
            'codigo postal',
            'numero de telefono',
            'mail',
            'web'
        ]
        

        return df[column_list]