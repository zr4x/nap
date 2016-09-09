class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("email_users").click()
        wd.find_element_by_name("email_users").clear()
        wd.find_element_by_name("email_users").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector("button.send_password").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_css_selector("div.content.center_align").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath(".//*[@id='logout']/a")) > 0

    def is_logged_in_as(self, username="Admin Napoleon" ):
        wd = self.app.wd
        return wd.find_element_by_xpath(".//*[@id='setting_menu']/span").text == username

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username="Admin Napoleon"):
                return
            else:
                self.logout()
        self.login(username, password)


