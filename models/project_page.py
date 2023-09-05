from selene import browser
from selene.support.conditions import have, be

class ProjectPage:

    def check_link_spb(self):
        browser.element('.skks-SPB').should(be.visible)

    def check_link_moscow(self):
        browser.element('.skks-Moscow').should(be.visible)