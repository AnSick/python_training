# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(maxlen):
    numbers =string.digits+"+()-"+" "*5
    return "".join([random.choice(numbers) for i in range(random.randrange(maxlen))])

testdata = [Contact(first_name="", middle_name="", last_name="", nickname="", title="",
                               company="", address="", home_number="",
                               mobile_number="", email="", website="", notes="",
                               work_number="", fax="", email2="", email3="", day_of_birth="3",
                               month_of_birth="2", birth_year="",
                               day_of_anniversary="3", month_of_anniversary="2", anniversary_year="",
                               address2="", phone2="",
                               photo="C:\\Workspace\\Python\\python_training\\hola.png")] + [
            Contact(first_name=random_string("first_name",10), middle_name=random_string("middle_name",10),
                    last_name=random_string("last_name",10), nickname=random_string("nickname",10),
                               title=random_string("title",10),
                               company=random_string("company",10), address=random_string("address",30),
                               home_number=random_number(20),
                               mobile_number=random_number(20), email=random_string("email",15),
                               website=random_string("website",20), notes=random_string("notes",40),
                               work_number=random_number(20), fax=random_string("fax",10),
                               email2=random_string("email2",20), email3=random_string("email3",20),
                               day_of_birth="1", month_of_birth="1", birth_year=random_number(4),
                               day_of_anniversary="1", month_of_anniversary="1", anniversary_year=random_number(4),
                               address2=random_string("address2",20), phone2=random_number(10),
                               photo="C:\\Workspace\\Python\\python_training\\hola.png"
                    )
for i in range(5)

]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    contact = Contact(first_name="", middle_name="", last_name="", nickname="", title="",
#                               company="", address="", home_number="",
#                               mobile_number="", email="", website="", notes="",
#                               work_number="", fax="", email2="", email3="", day_of_birth="3",
#                               month_of_birth="2", birth_year="",
#                               day_of_anniversary="3", month_of_anniversary="2", anniversary_year="",
#                               address2="", phone2="",
#                               photo="C:\\Workspace\\Python\\python_training\\hola.png")
#    old_contacts = app.contact.get_contact_list()
#    app.contact.create(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
