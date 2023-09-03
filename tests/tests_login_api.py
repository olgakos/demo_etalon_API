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
    assert type(response.json()['result']['expires_in']) == int


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


def test_login_negative_datatype():
    data = {
        'email': 'arven_test@etalongroup.com',
        'password': '8Y*m8DthaeSn',
        'user_id': 293

    }
    response = requests.post(
        url='https://dev0skks.etalongroup.com/auth/login',
        data = data
    )
    assert type(response.json()['result']['user_id']) == int, 'Ожидаемый тип данных: int'
    assert type(response.json()['result']['user_id']) != str