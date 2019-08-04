import unittest
import requests
import json

class TestApp(unittest.TestCase):
    def test_imports_good(self):
        url = 'http://localhost:8080/imports'
        data = {
        "citizens": [{
        "citizen_id": 1,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "appartement": 7,
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
        "appartement": 7,
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
        "appartement": 7,
        "name": "Иванов Иван Иванович",
        "birth_date": "01.02.2000",
        "gender": "male",
        "relatives": [1, 2]
        }]
        }
        r = requests.post(url, json=data)
        self.assertEqual(r.status_code, 201)
        #print(json.loads(r.content))
        self.import_id = json.loads(r.content)["data"]["import_id"]

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()
