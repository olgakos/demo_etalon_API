import os
from selene import browser

from models.login_page import LoginPage
from models.home_page import HomePage
from models.project_page import ProjectPage

#В идеале, для этого теста шаги, связанные с Залогином, можно вынести в TestBase.
#Но поскольку тест дополнительный, не делаю этого.

loginpage = LoginPage()
homepage = HomePage()
projectpage = ProjectPage()

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

def test_projects_page_available():
    browser.open('/')
    loginpage.type_login(login)
    loginpage.type_password(password)
    loginpage.press_loginbutton()
    homepage.check_title_DOM()
    browser.open('#!/app/core/projects///')
    projectpage.check_link_spb()
    projectpage.check_link_moscow()