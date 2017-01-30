class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.go_to_add_contact()
        # Create new contact
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_homepage()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.app.change_field_value("firstname", contact.first_name)
        self.app.change_field_value("middlename", contact.middle_name)
        self.app.change_field_value("lastname", contact.last_name)
        self.app.change_field_value("nickname", contact.nickname)
        self.app.change_field_value("title", contact.title)
        self.app.change_field_value("company", contact.company)
        self.app.change_field_value("address", contact.address)
        self.app.change_field_value("home", contact.home_number)
        self.app.change_field_value("mobile", contact.mobile_number)
        if contact.photo is not None:
            wd.find_element_by_css_selector('input[type="file"]').send_keys(
                contact.photo)
        self.app.change_field_value("work", contact.work_number)
        self.app.change_field_value("fax", contact.fax)
        self.app.change_field_value("email2", contact.email2)
        self.app.change_field_value("email3", contact.email3)
        self.app.change_field_value("email", contact.email)
        self.app.change_field_value("homepage", contact.website)
        # Reformat dates of birth and anniversary
        if contact.day_of_birth is not None:
            contact.day_of_birth = str(int(contact.day_of_birth) + 2)
            if not wd.find_element_by_xpath(
                            "//div[@id='content']/form/select[1]//option[%s]" % contact.day_of_birth).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % contact.day_of_birth).click()

        if contact.month_of_birth is not None:
            contact.month_of_birth = str(int(contact.month_of_birth) + 1)
            if not wd.find_element_by_xpath(
                            "//div[@id='content']/form/select[2]//option[%s]" % contact.month_of_birth).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % contact.month_of_birth).click()

        if contact.day_of_anniversary is not None:
            contact.day_of_anniversary = str(int(contact.day_of_anniversary) + 2)
            if not wd.find_element_by_xpath(
                            "//div[@id='content']/form/select[3]//option[%s]" % contact.day_of_anniversary).is_selected():
                wd.find_element_by_xpath(
                    "//div[@id='content']/form/select[3]//option[%s]" % contact.day_of_anniversary).click()

        if contact.month_of_anniversary is not None:
            contact.month_of_anniversary = str(int(contact.month_of_anniversary) + 1)
            if not wd.find_element_by_xpath(
                            "//div[@id='content']/form/select[4]//option[%s]" % contact.month_of_anniversary).is_selected():
                wd.find_element_by_xpath(
                    "//div[@id='content']/form/select[4]//option[%s]" % contact.month_of_anniversary).click()

        self.app.change_field_value("byear", contact.birth_year)
        self.app.change_field_value("ayear", contact.anniversary_year)
        self.app.change_field_value("address2", contact.address2)
        self.app.change_field_value("phone2", contact.phone2)
        self.app.change_field_value("notes", contact.notes)

    def count(self):
        wd=self.app.wd
        self.app.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    def go_to_add_contact(self):
        wd = self.app.wd
        # Go to contact creation form
        if not wd.current_url.endswith("/edit.php"):
            wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # check the first contact
        # submit
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        wd.switch_to_alert().accept()
        self.app.return_to_homepage()


    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="maintable"]/tbody/tr[2]/td[8]/a').click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.app.return_to_homepage()

    def delete_contact(self, contactNumber):
        wd = self.app.wd
        # check the first contact
        # submit
        wd.find_element_by_xpath("//*[@value=%s]" % contactNumber).click()
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        wd.switch_to_alert().accept()
        self.app.return_to_homepage()


    def edit_contact(self, contactNumber):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/edit.php?id=%s" % contactNumber)
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Goochi")
        wd.find_element_by_name("update").click()
        self.app.return_to_homepage()