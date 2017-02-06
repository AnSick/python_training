from model.contact import Contact
from random import randrange
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test", last_name="test"))
    old_contacts =db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

    def clean(contact):
        return Contact(id=contact.id, first_name=contact.first_name.strip(), last_name=contact.first_name.strip() )

    if check_ui:
        assert sorted(map(clean, new_contacts), key=Contact.id_or_max) == sorted(
            map(clean, app.contact.get_contact_list()), key=Contact.id_or_max)


#def test_delete_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first_name="test", last_name="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.delete_contact(25)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) - 1 == len(new_contacts)