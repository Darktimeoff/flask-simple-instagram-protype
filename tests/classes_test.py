import pytest
import json
import os

from classes.dao import Dao

class TestDao:
    def test_path_type_error(self):
        with pytest.raises(TypeError):
            Dao(1)  # type: ignore
    
    def test_path_value_error(self):
        with pytest.raises(ValueError):
            Dao('')
    
    def test_get_path_value(self):
        path = '/data/candidates.json'

        assert Dao(path).get_path() == path, 'Неверный путь'
    
    def test_load_data_not_foud_error(self):
        with pytest.raises(FileNotFoundError):
            Dao('/asdasd/').load_data()
    
    def test_load_data_decoded_error(self):
        with pytest.raises(json.decoder.JSONDecodeError):
            path = 'error.json'
            with open(path, 'w', encoding='utf-8') as file:
                file.write("{'a': 1,}")
                try:
                    Dao(path).load_data()
                finally:
                    if os.path.exists(path):
                        os.remove(path)