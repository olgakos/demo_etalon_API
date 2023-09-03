from selene import browser, have, be

login = 'arven_test@etalongroup.com'
password = '8Y*m8DthaeSn'
password_bad = '123456'

def test_login_ui():
    browser.open('/')
    browser.element('.form-login').should(have.text('Авторизация'))
    browser.element('[name=email]').type(login)
    browser.element('#passInput').type(password)
    browser.element('.btn-primary').click()
    browser.element('#sidebar').should(have.text('Ундомиэль Арвен null'))


def test_login_ui_bad():
    browser.open('/')
    browser.element('.form-login').should(have.text('Авторизация'))
    browser.element('[name=email]').type(login)
    browser.element('#passInput').type(password_bad)
    browser.element('.btn-primary').click()
    browser.element('.toast').should(have.text('проверьте правильность логина и пароля'))


def test_login_ui_bad_username():
    browser.open('/')
    browser.element('.form-login').should(have.text('Авторизация'))
    browser.element('[name=email]').type(login)
    browser.element('#passInput').type(password)
    browser.element('.btn-primary').click()
    browser.element('#sidebar').should(have.no.text('Фродо Бэггинс'))


def test_projects_page_available():
    browser.open('/')
    browser.element('.form-login').should(have.text('Авторизация'))
    browser.element('[name=email]').type(login)
    browser.element('#passInput').type(password)
    browser.element('.btn-primary').click()
    browser.element('#sidebar').should(have.text('Ундомиэль Арвен null'))
    browser.open('#!/app/core/projects///')
    browser.element('.skks-SPB').should(be.visible)
    browser.element('.skks-Moscow').should(be.visible)