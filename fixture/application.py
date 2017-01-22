from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper


class Application():
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)


    def return_to_groups_page(self):
        wd = self.wd
        # Return to groups page
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # Init group creation
        wd.find_element_by_name("new").click()
        # Fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.wd
        # Open groups page
        wd.find_element_by_link_text("groups").click()



    def open_homepage(self):
        wd = self.wd
        # Open homepage
        wd.get("http://localhost/addressbook/")

    def return_to_homepage(self):
        wd = self.wd
        # Return to home page
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, contact):
        wd = self.wd
        self.go_to_add_contact()
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
        # Reformat dates of birth and anniversary
        contact.day_of_birth = str(int(contact.day_of_birth) + 2)
        contact.month_of_birth = str(int(contact.month_of_birth) + 1)
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
        self.return_to_homepage()

    def go_to_add_contact(self):
        wd = self.wd
        # Go to contact creation form
        wd.find_element_by_link_text("add new").click()

    def destroy(self):
        self.wd.quit()