from jsonschema import validate
from utils import parse_date, get_current_date

SCHEMA_CITIZENS = {
    "definitions": {
        "citizen" : {
            "type" : "object",
            "properties": {
                "citizen_id" : {
                    "type" : "integer",
                    "minimum" : 0
                },
                "town" : {
                    "type" : "string",
                    "minLength": 1,
                    "maxLength": 256,
                },
                "street" : {
                    "type" : "string",
                    "minLength": 1,
                    "maxLength": 256,
                },
                "building" : {
                    "type" : "string",
                    "minLength": 1,
                    "maxLength": 256,
                },
                "apartment" : {
                    "type" : "integer",
                    "minimum" : 0
                },
                "name" : {
                    "type" : "string",
                    "minLength": 1,
                    "maxLength": 256,
                },
                "birth_date" : {
                    "type" : "string",
                    "pattern" : "^[0-9]{2}\.[0-9]{2}\.[0-9]{4}$",
                    "format" : "date"
                },
                "gender" : {
                    "type" : "string",
                    "pattern" : "^(male|female)$"
                },
                "relatives" : {
                    "type" : "array",
                    "items" : {
                        "type": "integer",
                        "minimum" : 0,
                    }
                }
            },
            "additionalProperties": False,
            "required" : [
                'citizen_id',
                'town',
                'street',
                'building',
                'apartment',
                'name',
                'birth_date',
                'gender',
                'relatives'
            ]
        }
    },
    "type" : "object",
    "properties" :  {
        "citizens" : {
            "type" : "array",
            "items" : { "$ref" : "#/definitions/citizen"}
        }
    },
    "additionalProperties": False,
    "required" : [
        "citizens"
    ]
}


SCHEMA_PATCH = {
    "type" : "object",
    "properties" : {
        "town" : {
            "type" : "string",
            "minLength": 1,
            "maxLength": 256,
        },
        "street" : {
            "type" : "string",
            "minLength": 1,
            "maxLength": 256,
        },
        "building" : {
            "type" : "string",
            "minLength": 1,
            "maxLength": 256,
        },
        "apartment" : {
            "type" : "integer",
            "minimum" : 0,
        },
        "name" : {
            "type" : "string",
            "minLength": 1,
            "maxLength": 256,
        },
        "birth_date" : {
            "type" : "string",
            "pattern" : "^[0-9]{2}\.[0-9]{2}\.[0-9]{4}$",
            "format" : "date"
        },
        "gender" : {
            "type" : "string",
            "pattern" : "^(male|female)$"
        },
        "relatives" : {
            "type" : "array",
            "items" : {
                "type": "integer",
                "minimum" : 0,
            }
        }
    },
    "minProperties": 1,
    "additionalProperties": False,
}


def validate_imports(data):
    validate(data, SCHEMA_CITIZENS)
    citizens = {}
    for citizen in data['citizens']:
        citizens[citizen['citizen_id']] = {'birth_date': citizen['birth_date'], 'relatives': citizen['relatives']}

        # check own id in relatives
        assert citizen['citizen_id'] not in citizen['relatives']
    
    # unique citizen_id check
    assert len(citizens) == len(data['citizens'])

    for cid, citizen in citizens.items():
        # check correct date
        assert get_current_date() > parse_date(citizen['birth_date'])
        
        #check correct relatives
        for relative in citizen['relatives']:
            assert cid in citizens[relative]['relatives']


def validate_patch(data):
    validate(data, SCHEMA_PATCH)
    assert get_current_date() > parse_date(data['birth_date'])


if __name__ == "__main__":
    a = {
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

    validate_imports(a)