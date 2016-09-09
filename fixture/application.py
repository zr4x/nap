from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.issue import IssueHeleper


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.session = SessionHelper(self)
        self.issue = IssueHeleper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://demopanel.napoleonit.ru/")

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()