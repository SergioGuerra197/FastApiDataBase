import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base #Sirve para manipular tablas de la base de datos

sqlite_file_name = '../database.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))#Le pasa la direccion del directorio actual

database_url = f'sqlite:///{os.path.join(base_dir, sqlite_file_name)}'#Join une las 2 variables

engine = create_engine(database_url, echo=True)#echo muestra por consola lo que se esta realizando

Session = sessionmaker(bind=engine)

Base = declarative_base()