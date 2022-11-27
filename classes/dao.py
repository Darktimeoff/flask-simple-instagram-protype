import json
import logging


class Dao:
    __path: str = ''

    def __init__(self, path: str):
        if type(path) is not str:
            raise TypeError("path must be a string")

        if not path:
            raise ValueError('path arg not defined')

        self.__path = path

    def get_path(self):
        return self.__path

    def load_data(self) -> list[dict]:
        with open(self.__path, 'rt', encoding='utf-8') as file:
            return json.load(file)
      
    def get_all(self):
        return self.load_data()
