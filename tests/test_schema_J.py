import requests
from jsonschema.validators import validate

def test_1():
    data1 = 'abc'

    response = requests.get(
        url="https://dev0skks.etalongroup.com",
        params={"title": "SKKS API - Auth"}
    )

