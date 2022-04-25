import click
import pandas as pd
from constanst import CSVS_DIR
import logging
from cfg import (
    museo_ds,
    cines_ds,
    bibliotecas_ds,
)

from extractors import(
    MuseoExtractor,
    BibliotecaExtractor,
    CineExtractor
)

from loaders import (
    BaseLoader,
    CineInsightsLoader,
    CantCategoriaLoader,
    CantProvCategoria,
    CantFuenteLoader
)


log = logging.getLogger()

extractores_diccionario = {
    'museo' : MuseoExtractor(museo_ds['name'], museo_ds['url']),
    'cines' : CineExtractor(cines_ds['name'], cines_ds['url']),
    'bibliotecas' : BibliotecaExtractor(bibliotecas_ds['name'], bibliotecas_ds['url']),
}

def extraer_datos(date_str: str) -> list[str]:
    paths_csvs = dict()
    for name, extractor in extractores_diccionario.items():
        file_path = extractor.extract(date_str)
        paths_csvs[name] = file_path

    return paths_csvs

def merge_csv(paths_csvs: list[str], path_file: str) -> str:
    transformados = list()

    for name, extractor in extractores_diccionario.items():
        df = pd.read_csv(paths_csvs[name])

        df_transformado = extractor.transform(df)
        transformados.append(df_transformado)

        pd.concat(transformados, axis=0).to_csv(path_file)

    print('\n LLEGO \n')
    return path_file


@click.command()
@click.option('--date', help= 'run date in format yyyy-mm-dd')
def run_pipeline(date: str) -> None:
    #Extract 
    log.info('Extracting')
    paths_csvs = extraer_datos(date)

    #transform
    merge_path = CSVS_DIR / 'merge_df_{date}.csv'
    merge_csv(paths_csvs, merge_path)

    #load
    log.info('Loading')
    BaseLoader().load_table(merge_path)
    CineInsightsLoader().load_table(paths_csvs['cines'])
    CantCategoriaLoader().load_table(merge_path)
    CantProvCategoria().load_table(merge_path)
    CantFuenteLoader().load_table(paths_csvs)

    log.info('Done')


if __name__ == '__main__':
    run_pipeline()