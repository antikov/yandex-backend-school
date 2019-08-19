import requests
import json
import pytest

@pytest.mark.incremental
class TestImports:
    def test_connect(self):
        url = 'http://0.0.0.0:8080/'
        r = requests.get(url)
        assert r.status_code == 404

    def test_good_import(self):
        url = 'http://0.0.0.0:8080/imports'
        data = {
        "citizens": [{
        "citizen_id": 1,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "apartment": 7,
        "name": "Иванов Иван Иванович",
        "birth_date": "01.02.2000",
        "gender": "male",
        "relatives": [2, 28]
        },
        {
        "citizen_id": 2,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "apartment": 7,
        "name": "Иванов Иван Иванович",
        "birth_date": "01.02.2000",
        "gender": "male",
        "relatives": [1, 28]
        },
        {
        "citizen_id": 28,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "apartment": 7,
        "name": "Иванов Иван Иванович",
        "birth_date": "01.02.2000",
        "gender": "male",
        "relatives": [1, 2]
        }]
        }
        r = requests.post(url, json=data)
        assert r.status_code == 201
