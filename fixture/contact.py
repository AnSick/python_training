from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.go_to_add_contact()
        # Create new contact
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_homepage()
        self.contact_cache = None

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
        self.delete_some_contact(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # check the first contact
        # submit
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        wd.switch_to_alert().accept()
        self.app.open_homepage()
        self.contact_cache = None


    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.modify_contact_by_index(0)


    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
       # stro = "//*[@id=\"maintable\"]/tbody/tr[" + str(index+1) + "]/td[8]/a"
        #wd.find_element_by_xpath(stro).click()
        entry_element = wd.find_elements_by_name("entry")[index]
        entry_element.find_elements_by_tag_name("td")[7].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.app.open_homepage()
        self.contact_cache = None

    #def delete_contact(self, contactNumber):
    #    wd = self.app.wd
        # check the first contact
        # submit
    #    wd.find_element_by_xpath("//*[@value=%s]" % contactNumber).click()
    #    wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
    #    wd.switch_to_alert().accept()
    #    self.app.open_homepage()


    #def edit_contact(self, contactNumber):
    #    wd = self.app.wd
    #    wd.get("http://localhost/addressbook/edit.php?id=%s" % contactNumber)
    #    wd.find_element_by_name("firstname").click()
    #    wd.find_element_by_name("firstname").clear()
    #    wd.find_element_by_name("firstname").send_keys("Goochi")
    #    wd.find_element_by_name("update").click()
    #    self.app.open_homepage()


    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                data = element.find_elements_by_tag_name("td")
                first_name = data[2].text
                last_name = data[1].text
                address = data[3].text
                all_emails = data[4].text
                all_phones = data[5].text
                self.contact_cache.append(Contact(first_name = first_name, last_name = last_name, id = id,
                                                  all_phones_from_home_page = all_phones, address=address, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage()
        entry_element = wd.find_elements_by_name("entry")[index]
        cell = entry_element.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_view_contact_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage()
        entry_element = wd.find_elements_by_name("entry")[index]
        cell = entry_element.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home_number = wd.find_element_by_name("home").get_attribute("value")
        work_number = wd.find_element_by_name("work").get_attribute("value")
        mobile_number = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        return Contact(first_name=first_name, last_name=last_name, home_number=home_number,
                       work_number=work_number, mobile_number=mobile_number, phone2=phone2,
                       id=id, address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_view_contact_page_by_index(index)
        text = wd.find_element_by_id("content").text
        home_number = re.search("H: (.*)", text).group(1)
        mobile_number = re.search("M: (.*)", text).group(1)
        work_number = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_number=home_number, mobile_number=mobile_number, work_number=work_number, phone2=phone2)

