from decouple import AutoConfig
from constanst import  ROOT_DIR

config = AutoConfig(search_path = ROOT_DIR)

URL_DB = config('URL_DB' )
MUSEO_URL = config('MUSEO_URL')
CINES_URL = config('CINES_URL')
ESPACIOS_URL = config('ESPACIOS_URL')

museo_ds = {
    'name' : 'museo',
    'url': MUSEO_URL,
}

cines_ds = {
    'name' : 'cines_',
    'url': CINES_URL,
}

espacios_ds = {
    'name' : 'espacios',
    'url': ESPACIOS_URL,
}
