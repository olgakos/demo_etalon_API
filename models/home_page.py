from selene import browser
from selene.support.conditions import have, be

class HomePage:

    def check_username(self, s):
        browser.element('#sidebar').should(have.text(s))

    def check_title_DOM(self):
        browser.should(have.title_containing('SKKS App - Дашборд'))



    def check_username_bad(self, s):
        browser.element('#sidebar').should(have.no.text(s))
