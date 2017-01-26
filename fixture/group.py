class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        # Return to groups page
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
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
        wd = self.app.wd
        # Open groups page
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        #select first group
        #submit deletion
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()


    def edit_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        #select first group
        #submit edit
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("GET CHANGED")
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_group(self, groupnumber):
        wd = self.app.wd
        self.open_groups_page()
        #select a group by identificator from database
        #submit deletion
        wd.find_element_by_xpath("//*[@value=%s]" % groupnumber).click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()


    def edit_group(self, groupNumber):
        wd = self.app.wd
        self.open_groups_page()
        #select a group by identificator from database
        #submit edit
        wd.find_element_by_xpath("//*[@value=%s]" % groupNumber).click()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("GET CHANGED")
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()