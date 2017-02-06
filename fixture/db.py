import mysql.connector
from model.group import Group
from model.contact import Contact

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name =  name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host = host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, "
                           "home, mobile, work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear, "
                           "address2, phone2, notes, photo from addressbook where deprecated > NOW() or deprecated is null")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address,
                 home, mobile, work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear,
                 address2, phone2, notes, photo) = row
                list.append(Contact(id=str(id), first_name=firstname, middle_name=middlename, last_name=lastname, nickname=nickname, company=company, title=title,
                                    address=address, website=homepage, home_number=home, mobile_number=mobile, work_number=work, fax=fax, email=email, email2=email2, email3=email3,
                                    day_of_birth=bday, month_of_birth=bmonth, birth_year=byear, day_of_anniversary=aday, month_of_anniversary=amonth, anniversary_year=ayear,
                                    address2=address2, phone2=phone2, notes=notes, photo=photo))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()