from constanst import CSVS_DIR
from datetime import datetime
import requests 
import logging
import pandas as pd

log = logging.getLogger()

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


class UrlExtractor:
    path_model =(
        '{category}/{year}-{month:02d}/{category}-{day:02d}-{month:02d}-{year}.csv'
    )

    def __init__(self, name, url) -> None:
        self.name = name
        self.url = url

    def extract(self, date_str) -> str:
        
        log.info(f'Extrayendo {self.name}')
        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        file_path = self.path_model.format(
            category=self.name, year = date.year, month = date.month, day = date.day
        )
        m_path = CSVS_DIR / file_path
        m_path.parent.mkdir(parents=True, exist_ok= True)

        r = requests.get(self.url)
        r.encoding = 'utf-8'

        log.info(f'Guardando {m_path}')
        with open(m_path, 'w', encoding="utf-8") as f_out:
            f_out.write(r.text)

        return m_path

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

class BibliotecaExtractor(UrlExtractor):
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:

        rename_columns = {
            'Cod_Loc' : 'cod_localidad',
            'IdProvincia' : 'id_provincia',
            'IdDepartamento' : 'id_departamento',
            'Categoría' : 'categoria',
            'Provincia' : 'provincia',
            'Localidad' : 'localidad',
            'Nombre' : 'nombre',
            'Domicilio' : 'domicilio',
            'CP' : 'codigo postal',
            'Teléfono' : 'numero de telefono',
            'Mail' : 'mail',
            'Web' : 'web'
        }

        df = df.rename(columns= rename_columns)

        return df[column_list]

class MuseoExtractor(UrlExtractor):
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:

        rename_columns = {
            'Cod_Loc' : 'cod_localidad',
            'IdProvincia': 'id_provincia',
            'IdDepartamento' : 'id_departamento',
            'direccion' : 'domicilio',
            'CP' : 'codigo postal',
            'telefono' : 'numero de telefono',
            'Mail' : 'mail',
            'Web': 'web',
        }

        df = df.rename(columns= rename_columns)

        return df[column_list]


class CineExtractor(UrlExtractor):
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:

        rename_columns = {
            'Cod_Loc' : 'cod_localidad',
            'IdProvincia' : 'id_provincia',
            'IdDepartamento' : 'id_departamento',
            'Categoría' : 'categoria',
            'Provincia' : 'provincia',
            'Localidad' : 'localidad',
            'Nombre' : 'nombre',
            'Dirección' : 'domicilio',
            'CP' : 'codigo postal',
            'Teléfono' : 'numero de telefono',
            'Mail' : 'mail',
            'Web' : 'web'
        }

        df = df.rename(columns= rename_columns)

        return df[column_list]