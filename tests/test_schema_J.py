import requests

def test_positive_login():
    data = {
        'email': 'arven_test@etalongroup.com',
        'password': '8Y*m8DthaeSn'
    }
    response = requests.post(
        url='https://dev0skks.etalongroup.com/auth/login',
        data = data
    )
    assert response.status_code == 200, 'Ошибка при позитивном тесте'
    assert response.json()['ok'] == True
    assert response.json()['result']['user_id'] == 293
    assert response.json()['result']['token_type'] == 'Bearer'
    assert type(response.json()['result']['access_token']) == str
    assert type(response.json()['result']['expires_in']) == int  #"expires_in":25856

    # assert response.json()['result': {{"user_id":293,''
    #                                    "token_type":"Bearer",
    #                                    "access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJza2tzIiwianRpIjoiMTg4MjgiLCJleHAiOjE2OTM3MDI4MDAsInVpZCI6MjkzfQ.OYavSt4-3_KoXZ29vPFo09ZX_K53hP8CXZv-3joJLp2tdh0QvLMUW8ekPHgcNGS_Qc5tEBOsOz8VmOaR6bFcnrTS02l3c-aAT5-FbiDQULDDsajVQ_4-xrMn_rYKrWa8bQ61yYzjRmAtBe9ohzcLhDRX43AIrcLWx_qyqWWEyLdNUGKtUxMH1K5yIFDj6wUodGDePxkVnE3k6-_8DkgsrQFeGwUd4K6pPb1FBe6TQ8LrwB6MY77XkArtcAQN6-J9CN5ac61j3elhLt4dW0-SOsindnNknwcaX7GPqDMsAjb44CBsvzLkZdHmWjYEmAnop94_IC1yql0mTCNkT6xLkg",
    #                                    "expires_in":26517}}}] == True


def test_login_negative_method_put():
    data = {
        'email': 'arven_test@etalongroup.com',
        'password': '8Y*m8DthaeSn'
    }
    response = requests.put(
        url='https://dev0skks.etalongroup.com/auth/login',
        data = data
    )
    assert response.status_code == 405, 'Метод запроса известен серверу, но был отключён и не может быть использован'


def test_login_negative_path():
    data = {
        'email': 'arven_test@etalongroup.com',
        'password': '8Y*m8DthaeSn'
    }
    response = requests.post(
        url='https://dev0skks.etalongroup.com/auth/log',
        data = data
    )
    assert response.status_code == 404, 'Не найден путь: /auth/log'

def test_login_access_token_type():
    data = {
        'email': 'arven_test@etalongroup.com',
        'password': '8Y*m8DthaeSn'
    }
    response = requests.post(
        url='https://dev0skks.etalongroup.com/auth/login',
        data = data
    )
    assert response.status_code == 200, 'Ошибка при позитивном тесте'
    assert response.json()['ok'] == True
    assert response.json()['result']['user_id'] == 293
    assert response.json()['result']['token_type'] == 'Bearer'
    assert type(response.json()['result']['access_token']) == int #Expected :<class 'int'> Actual :<class 'str'>
    # assert