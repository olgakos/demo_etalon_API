import requests

def test_url_status_code():
    response = requests.get("https://dev0skks.etalongroup.com")
    print(type(response))
    print(response.status_code)
    print(response.json)

    assert response.status_code == 200


#(venv) D:\PythonParty\demo_etalon_API>pytest tests\tests_requests1.py -s
