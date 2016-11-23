from selenium.webdriver.common.action_chains import *


class IssueHeleper:
    def __init__(self, app):
        self.app = app

    # def edit_first_issue(self):
    #     wd = self.app.wd
    #     wd.ActionChains
    #     wd.find_element_by_xpath("html/body/div[3]/table/tbody/tr[2]/td[9]/a").click()

    def fill_issue_form(self, issue):
        self.sorry()
        self.change_field_value("name_issue", issue.name)
        self.change_field_value("text_issue", issue.description)
        self.change_field_value("product_id", issue.product_id)
        self.change_field_value("day", issue.day)
        self.change_field_value("month", issue.month)
        self.change_field_value("year", issue.year)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

# РЕАЛИЗОВАЛ КЛИК МЫШКОЙ ПО ЭЛЕМЕНТУ
    def sorry(self):
        wd = self.app.wd
        menu = wd.find_element_by_xpath("html/body/div[3]/table/tbody/tr[2]/td[5]")
        hidden_subtend = wd.find_element_by_xpath("html/body/div[3]/table/tbody/tr[2]/td[9]/a")
        ActionChains(wd).move_to_element(menu).click(hidden_subtend).perform()