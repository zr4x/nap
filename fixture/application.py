from selenium import webdriver
from fixture.session import SessionHelper
from fixture.issue import IssueHeleper


class Application:
    def __init__(self, url):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.issue = IssueHeleper(self)
        self.url = url

    def open_home_page(self):
        wd = self.wd
        wd.get(self.url)
        wd.implicitly_wait(10)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()