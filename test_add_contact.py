# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_contact(self):
        wd = self.wd
        self.login(wd)
        self.create_contact(wd,
                            Contact(first_name="Kim2", middle_name="Woo", last_name="Bin", nickname="bigbangtheory13",
                                    title="leading software engineer",
                                    company="SBS Entertainment", address="Songnam-gu, 145-12, Okchomdang, Seoul",
                                    home_number="713 823-52-32",
                                    mobile_number="010-352-51-32", email="sunnykimwoobit@gmail.co.kr",
                                    website="kimwoobin.co.kr", notes="Handsome and sweet",
                                    work_number="512 09 56", fax="3321", email2="dagaga", email3="agsagsag",
                                    day_of_birth="1", month_of_birth="1", birth_year="1994",
                                    day_of_anniversary="1", month_of_anniversary="1", anniversary_year="4131",
                                    address2="hjfkhaskfjsaf", phone2="jsfahsfjksaf",
                                    photo="C:\\Workspace\\Python\\python_training\\hola.png"))
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.login(wd)
        self.create_contact(wd, Contact(first_name="", middle_name="", last_name="", nickname="", title="",
                                        company="", address="", home_number="",
                                        mobile_number="", email="", website="", notes="",
                                        work_number="", fax="", email2="", email3="", day_of_birth="3",
                                        month_of_birth="2", birth_year="",
                                        day_of_anniversary="3", month_of_anniversary="2", anniversary_year="",
                                        address2="", phone2="",
                                        photo="C:\\Workspace\\Python\\python_training\\hola.png"))
        self.logout(wd)

    def logout(self, wd):
        # Logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_homepage(self, wd):
        # Return to home page
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, wd, contact):
        self.go_to_add_contact(wd)
        # Create new contact
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_number)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_number)
        wd.find_element_by_css_selector('input[type="file"]').send_keys(
            contact.photo)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_number)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.website)
        #Reformat dates of birth and anniversary
        contact.day_of_birth = str(int(contact.day_of_birth) + 2)
        contact.month_of_birth = str(int(contact.month_of_birth) +1)
        contact.day_of_anniversary = str(int(contact.day_of_anniversary) + 2)
        contact.month_of_anniversary = str(int(contact.month_of_anniversary) + 1)
        if not wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[1]//option[%s]" % contact.day_of_birth).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % contact.day_of_birth).click()
        if not wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[2]//option[%s]" % contact.month_of_birth).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % contact.month_of_birth).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)
        if not wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[3]//option[%s]" % contact.day_of_anniversary).is_selected():
            wd.find_element_by_xpath(
                "//div[@id='content']/form/select[3]//option[%s]" % contact.day_of_anniversary).click()
        if not wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[4]//option[%s]" % contact.month_of_anniversary).is_selected():
            wd.find_element_by_xpath(
                "//div[@id='content']/form/select[4]//option[%s]" % contact.month_of_anniversary).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_homepage(wd)

    def go_to_add_contact(self, wd):
        # Go to contact creation form
        wd.find_element_by_link_text("add new").click()

    def login(self, wd):
        self.go_to_homepage(wd)
        # Login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def go_to_homepage(self, wd):
        # Go to home page
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
