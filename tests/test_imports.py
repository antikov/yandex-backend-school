import requests

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
print(r.status_code)
print(r.content)
print(r.headers)
