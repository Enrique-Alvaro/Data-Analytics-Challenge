from decouple import AutoConfig
from constanst import  ROOT_DIR


# instancio config diciendole donde tiene que buscar los valores para las variables
# levanto las variables
config = AutoConfig(search_path = ROOT_DIR)

# levanto las variables

URL_DB = config('URL_DB' )
MUSEO_URL = config('MUSEO_URL')
CINES_URL = config('CINES_URL')
ESPACIOS_URL = config('ESPACIOS_URL')


#creo diccionario

museo_ds = {
    #nombre de mi data_source
    'name' : 'museo',
    'url': MUSEO_URL,
}

cines_ds = {
    #nombre de mi data_source
    'name' : 'cines_',
    'url': CINES_URL,
}

espacios_ds = {
    #nombre de mi data_source
    'name' : 'espacios',
    'url': ESPACIOS_URL,
}
