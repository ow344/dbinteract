from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from os import environ
from dotenv import load_dotenv

load_dotenv('.env')

host = environ.get('host')
user = environ.get('user')
password = environ.get('password')
database = environ.get('database')

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}", echo=True)
session = Session(engine)


