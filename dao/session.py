import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Session:
    def __init__(self):
        load_dotenv()
        connector = os.getenv('CONNECTOR')
        host = os.getenv('HOST')
        user = os.getenv('USER')
        password = os.getenv('PASSWORD')
        dbname = os.getenv('DATABASE')
        self.__conn_string = f'{connector}://{user}:{password}@{host}:3306/{dbname}'

    def __enter__(self):
        self.__engine = create_engine(self.__conn_string)
        Session = sessionmaker(self.__engine)
        self.__session = Session()
        return self.__session

    def __exit__(self, type, value, traceback):
        self.__session.close()
        self.__engine.dispose()