import click
from extractors import MuseoExtractor, UrlExtractor
import pandas as pd
from constanst import BASE_FILE_DIR
from cfg import (
    museo_ds,
    cines_ds,
    espacios_ds,
)

from loaders import (
    CineInsightsLoader,
    SizeByCategoryLoader,
    SizeByCatProvLoader,
    SizeBySourceLoader
)

import logging


log = logging.getLogger()
extractors_dict = {
    'museo' : MuseoExtractor(museo_ds['name'], museo_ds['url']),
    'cines' : UrlExtractor(cines_ds['name'], cines_ds['url']),
    'espacios' : UrlExtractor(espacios_ds['name'], espacios_ds['url']),
}

def extract_raws(date_str: str) -> list[str]:
    file_paths = dict()
    for name, extractor in extractors_dict.items():
        file_path = extractor.extract(date_str)
        file_paths[name] = file_path
    return file_paths

def merge_raw(file_paths: list[str], out_file_path: str) -> str:
    dfs_transformed = list()

    for name, extractor in extractors_dict.items():
        df = pd.read_csv(file_paths[name])
        dft = extractor.transform(df)
        dfs_transformed.append(dft)
        pd.concat(dfs_transformed, axis=0).to_csv(out_file_path)
    return out_file_path


@click.command()
@click.option('--date', help= 'run date in format yyyy-mm-dd')
def run_pipeline(date: str) -> None:
    #Extract 
    log.info('Extracting')
    file_paths = extract_raws(date)

    #transform
    merge_path = BASE_FILE_DIR / 'merge_df_{date}.csv'
    merge_raw(file_paths, merge_path)

    #load
    log.info('Loading')
    CineInsightsLoader().load_table(file_paths['cines'])
    SizeByCategoryLoader().load_table(merge_path)
    SizeBySourceLoader().load_table(file_paths)
    SizeByCatProvLoader().load_table(merge_path)
    log.info('Done')


if __name__ == '__main__':
    run_pipeline()