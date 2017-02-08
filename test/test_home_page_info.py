import re
from random import randrange
from model.contact import Contact


def test_info_on_home_page(app):
    contacts_from_home_page = app.contact.get_contact_list()
    index = randrange(len(contacts_from_home_page))
    contact_from_home_page = contacts_from_home_page[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(number):
    return re.sub("[() -]", "", number)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
        map(lambda x: clear(x),
            filter(lambda x: x is not None,
                   [contact.home_number, contact.mobile_number,contact.work_number, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))


def test_info_of_all_contacts(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key= Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key = Contact.id_or_max)
    for i in range(0, len(contacts_from_home_page)):
        contact_home_page = contacts_from_home_page[i]
        contact_db = contacts_from_db[i]
        assert contact_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(
            contact_db)
        assert contact_home_page.first_name.strip() == contact_db.first_name.strip()
        assert contact_home_page.last_name.strip() == contact_db.last_name.strip()
        assert contact_home_page.address.strip() == contact_db.address.strip()
        assert contact_home_page.all_emails_from_home_page.replace(' ', '') == merge_emails_like_on_home_page(contact_db).replace(' ', '')
