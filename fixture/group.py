from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # Init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.open_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.app.change_field_value("group_name", group.name)
        self.app.change_field_value("group_header", group.header)
        self.app.change_field_value("group_footer", group.footer)

    #def change_field_value(self, field_name, text):
    #    wd = self.app.wd
    #    if text is not None:
    #        wd.find_element_by_name(field_name).click()
    #        wd.find_element_by_name(field_name).clear()
    #        wd.find_element_by_name(field_name).send_keys(text)

    def open_groups_page(self):
        wd = self.app.wd
        # Open groups page
        if not (wd.current_url.endswith("/groups.php") and len(wd.find_elements_by_name("new"))>0):
            wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.delete_group_by_index(0)


    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        #select first group
        #submit deletion
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        self.open_groups_page()
        self.group_cache = None


    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        #select first group
        #submit edit
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.open_groups_page()
        self.group_cache = None

    def modify_group_by_id(self, id, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        # submit edit
        self.select_group_by_id(id)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.open_groups_page()
        self.group_cache = None


    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value = '%s']" % id).click()



    #def delete_group(self, groupnumber):
    #    wd = self.app.wd
    #    self.open_groups_page()
        #select a group by identificator from database
        #submit deletion
    #    wd.find_element_by_xpath("//*[@value=%s]" % groupnumber).click()
    #    wd.find_element_by_name("delete").click()
    #    self.open_groups_page()


    #def edit_group(self, groupNumber):
    #    wd = self.app.wd
    #    self.open_groups_page()
        #select a group by identificator from database
        #submit edit
    #    wd.find_element_by_xpath("//*[@value=%s]" % groupNumber).click()
    #    wd.find_element_by_name("edit").click()
    #    wd.find_element_by_name("group_name").click()
    #    wd.find_element_by_name("group_name").clear()
    #    wd.find_element_by_name("group_name").send_keys("GET CHANGED")
    #    wd.find_element_by_name("update").click()
    #    self.open_groups_page()

    group_cache = None

    def get_group_list(self):

        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name = text, id = id))
        return list(self.group_cache)