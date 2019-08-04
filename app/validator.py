from jsonschema import validate
from utils import parse_date

SCHEMA_CITIZENS = {
    "definitions": {
        "citizen" : {
            "type" : "object",
            "properties": {
                "citizen_id" : {
                    "type" : "integer"
                },
                "town" : {
                    "type" : "string",
                    "minLength": 1
                },
                "street" : {
                    "type" : "string",
                    "minLength": 1
                },
                "building" : {
                    "type" : "string",
                    "minLength": 1
                },
                "appartement" : {
                    "type" : "integer"
                },
                "name" : {
                    "type" : "string",
                    "minLength": 1
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
                        "type": "integer"
                    }
                }
            },
            "required" : [
                'citizen_id',
                'town',
                'street',
                'building',
                'appartement',
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
    "required" : [
        "citizens"
    ]
}


SCHEMA_PATCH = {
}

def validate_imports(data):
    validate(data, SCHEMA_CITIZENS)

    citizens = {}
    for citizen in data:
        citizens[citizen['citizen_id']] = {'birth_date': citizen['birth_date'], 'relatives': citizen['relatives']}
    
    # unique citizen_id check
    assert len(citizens) == len(data)

    for cid, citizen in citizens.items():
        # check correct date
        parse_date(citizen['birth_date'])
        
        #check correct relatives
        for relative in citizen['relatives']:
            assert cid in citizens[relative]['relatives']


def validate_patch(data):
    validate(data, SCHEMA_PATCH)
