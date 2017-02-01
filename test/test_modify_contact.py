from model.contact import Contact
from random import randrange


def test_modify_some_contact_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(company="Peter-service")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_edit_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first_name="test"))
#    old_contacts = app.contact.get_contact_list()
#    #Edit contact by its identificator
#    app.contact.edit_contact(2)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
