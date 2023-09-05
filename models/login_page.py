from selene import browser, by
from selene.support.conditions import have, be

class LoginPage:


    def check_title_DOM(self):
        browser.should(have.title_containing('SKKS App - Охрана труда'))

    def check_title_page(self):
        browser.element('.form-login').should(have.text('Авторизация'))

    def type_login(self, s):
        browser.element('[name=email]').type(s)

    def type_password(self, s):
        browser.element('#passInput').type(s)

    def press_loginbutton(self):
        browser.element('.btn-primary').click()

    def check_password_bad(self):
        browser.element('.toast').should(have.text('проверьте правильность логина и пароля'))

