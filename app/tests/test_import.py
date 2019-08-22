import requests
import json
import pytest

@pytest.mark.incremental
class TestImports:
    @pytest.mark.parametrize("path,status", [
        ("/", 404),
        ("/imports", 405),
        ("/imports/0/citizens", 404),
    ])
    def test_connect(self, path, status):
        url = 'http://0.0.0.0:8080' + path
        r = requests.get(url)
        assert r.status_code == status

    @pytest.mark.parametrize("data, status", [
        # good import
        ({
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
        }, 201),
        # missing field "name"
        ({
        "citizens": [{
        "citizen_id": 1,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "apartment": "7",
        "birth_date": "01.02.2000",
        "gender": "male",
        "relatives": []
        }]
        }, 400),

        # empty good import
        ({
        "citizens": []
        }, 500),
  
        # new field "temp"
        ({
        "citizens": [{
        "name": "Иванов Иван Иванович",
        "temp" : "temp",
        "citizen_id": 1,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "apartment": "7",
        "birth_date": "01.02.2000",
        "gender": "male",
        "relatives": []
        }]
        }, 400),

        # bad format apartment
        ({
        "citizens": [{
        "citizen_id": 1,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "apartment": "7",
        "name": "Иванов Иван Иванович",
        "birth_date": "01.02.2000",
        "gender": "male",
        "relatives": []
        }]
        }, 400),

        # bad relatives #1
        ({
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
        }]
        }, 400),
        # bad relatives #2
        ({
        "citizens": [{
        "citizen_id": 1,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "apartment": 7,
        "name": "Иванов Иван Иванович",
        "birth_date": "01.02.2000",
        "gender": "male",
        "relatives": [1]
        }]
        }, 400),

        # bad date # 1
        ({
        "citizens": [{
        "citizen_id": 1,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "apartment": 7,
        "name": "Иванов Иван Иванович",
        "birth_date": "30.02.2000",
        "gender": "male",
        "relatives": []
        }]
        }, 400),
        # bad date # 2
        ({
        "citizens": [{
        "citizen_id": 1,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "apartment": 7,
        "name": "Иванов Иван Иванович",
        "birth_date": "12.34.5678",
        "gender": "male",
        "relatives": []
        }]
        }, 400),
        # bad date # 3
        ({
        "citizens": [{
        "citizen_id": 1,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "apartment": 7,
        "name": "Иванов Иван Иванович",
        "birth_date": "1.2.2002",
        "gender": "male",
        "relatives": []
        }]
        }, 400),
        # bad date # 4
        ({
        "citizens": [{
        "citizen_id": 1,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "apartment": 7,
        "name": "Иванов Иван Иванович",
        "birth_date": "31.04.2002",
        "gender": "male",
        "relatives": []
        }]
        }, 400),

    ])
    def test_import(self, data, status):
        url = 'http://0.0.0.0:8080/imports'
        r = requests.post(url, json=data)
        assert r.status_code == status
