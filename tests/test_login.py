import os

from selene import browser

from models.login_page import LoginPage
from models.home_page import HomePage

loginpage = LoginPage()
homepage = HomePage()

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

def test_login():
    username = 'Ундомиэль Арвен null'

    browser.open('/')
    loginpage.check_title_DOM()
    loginpage.check_title_page()
    loginpage.type_login(login)
    loginpage.type_password(password)
    loginpage.press_loginbutton()
    homepage.check_username(username)

def test_login_ui_bad():
    password_bad = '12345'

    browser.open('/')
    loginpage.check_title_DOM()
    loginpage.check_title_page()
    loginpage.type_login(login)
    loginpage.type_password(password_bad)
    loginpage.press_loginbutton()
    loginpage.check_password_bad()

def test_login_ui_bad_username():
    username_bad = 'Фродо Бэггинс'

    browser.open('/')
    loginpage.check_title_DOM()
    loginpage.check_title_page()
    loginpage.type_login(login)
    loginpage.type_password(password)
    loginpage.press_loginbutton()
    homepage.check_username_bad(username_bad)