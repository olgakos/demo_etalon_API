import json

import requests
import PyYAML
from jsonschema.validators import validate
from jsonschema.validators import validate
from yamlschema import validateYAML
#from yaml

# from schemas.schema_yaml.yaml import get1

def test_get_schema1():
    response = requests.get("https://dev0skks.etalongroup.com")
    # assert S(get1) == response.json()
