from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


settings  = {
    'pguser' :'postgres',
    'pgpassword' : '123',
    'pghost' : 'localhost' ,
    'pgport' : 5432,
    'pgdb' : 'data_analytics'
}

def get_engine(user, passwd, host, port, db):
    url = f'postgresql://{user}:{passwd}@{host}:{port}/{db}'

    if not database_exists(url):
        create_database(url)
    
    engine = create_engine(url, pool_size = 50, echo =False)
    return engine


engine = get_engine(settings['pguser'], 
                    settings['pgpassword'], 
                    settings['pghost'], 
                    settings['pgport'],
                    settings['pgdb'])

print(engine.url)

