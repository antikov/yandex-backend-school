import requests
import json
import pytest

def json_equal(a, b):
    a, b = json.dumps(a, sort_keys=True), json.dumps(b, sort_keys=True)
    return a == b

@pytest.fixture(scope="session")
def get_import_id():
    data = {
        "citizens": [
        {
        "citizen_id": 1,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "apartment": 7,
        "name": "Иванов Иван Иванович",
        "birth_date": "26.12.1986",
        "gender": "male",
        "relatives": [2]
        },
        {
        "citizen_id": 2,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "apartment": 7,
        "name": "Иванов Сергей Иванович",
        "birth_date": "01.04.1997",
        "gender": "male",
        "relatives": [1]
        },
        {
        "citizen_id": 3,
        "town": "Керчь",
        "street": "Иосифа Бродского",
        "building": "2",
        "apartment": 11,
        "name": "Романова Мария Леонидовна",
        "birth_date": "23.11.1986",
        "gender": "female",
        "relatives": []
        },
        ]
        }
    url = 'http://0.0.0.0:8080/imports'
    r = requests.post(url, json=data)
    assert r.status_code == 201
    import_id = r.json()['data']['import_id']
    assert import_id > 0
    return import_id

@pytest.mark.incremental
class TestPatch:

    def test_patch(self, get_import_id):
        import_id = get_import_id
        url = f'http://0.0.0.0:8080/imports/{import_id}/citizens/3'
        data = {
        "name": "Иванова Мария Леонидовна",
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "apartment": 7,
        "relatives": [1]
    }
        r = requests.patch(url, json=data)
        assert r.status_code == 200
        assert json_equal(r.json(),{
        "data": {
        "citizen_id": 3,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "apartment": 7,
        "name": "Иванова Мария Леонидовна",
        "birth_date": "23.11.1986",
        "gender": "female",
        "relatives": [1]
        }
        }
        )

    def test_citizens(self, get_import_id):
        import_id = get_import_id
        url = f'http://0.0.0.0:8080/imports/{import_id}/citizens'
        r = requests.get(url)
        assert r.status_code == 200
        assert json_equal(r.json(),{
    "data": [
    {
    "citizen_id": 1,
    "town": "Москва",
    "street": "Льва Толстого",
    "building": "16к7стр5",
    "apartment": 7,
    "name": "Иванов Иван Иванович",
    "birth_date": "26.12.1986",
    "gender": "male",
    "relatives": [2,3]
    },
    {
    "citizen_id": 2,
    "town": "Москва",
    "street": "Льва Толстого",
    "building": "16к7стр5",
    "apartment": 7,
    "name": "Иванов Сергей Иванович",
    "birth_date": "01.04.1997",
    "gender": "male",
    "relatives": [1]
    },
    {
    "citizen_id": 3,
    "town": "Москва",
    "street": "Льва Толстого",
    "building": "16к7стр5",
    "apartment": 7,
    "name": "Иванова Мария Леонидовна",
    "birth_date": "23.11.1986",
    "gender": "female",
    "relatives": [1]
    }
    ]
    }
    )

    def test_patch2(self, get_import_id):
        import_id = get_import_id
        url = f'http://0.0.0.0:8080/imports/{import_id}/citizens/3'
        data = {
            "relatives": []
        }
        r = requests.patch(url, json=data)
        assert r.status_code == 200
        assert json_equal(r.json(),{
            "data": {
            "citizen_id": 3,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "apartment": 7,
            "name": "Иванова Мария Леонидовна",
            "birth_date": "23.11.1986",
            "gender": "female",
            "relatives": []
            }
        })
    
    def test_citizens2(self, get_import_id):
        import_id = get_import_id
        url = f'http://0.0.0.0:8080/imports/{import_id}/citizens'
        r = requests.get(url)
        assert r.status_code == 200
        assert json_equal(r.json(),{
    "data": [
    {
    "citizen_id": 1,
    "town": "Москва",
    "street": "Льва Толстого",
    "building": "16к7стр5",
    "apartment": 7,
    "name": "Иванов Иван Иванович",
    "birth_date": "26.12.1986",
    "gender": "male",
    "relatives": [2]
    },
    {
    "citizen_id": 2,
    "town": "Москва",
    "street": "Льва Толстого",
    "building": "16к7стр5",
    "apartment": 7,
    "name": "Иванов Сергей Иванович",
    "birth_date": "01.04.1997",
    "gender": "male",
    "relatives": [1]
    },
    {
    "citizen_id": 3,
    "town": "Москва",
    "street": "Льва Толстого",
    "building": "16к7стр5",
    "apartment": 7,
    "name": "Иванова Мария Леонидовна",
    "birth_date": "23.11.1986",
    "gender": "female",
    "relatives": []
    }
    ]
    }
    )
