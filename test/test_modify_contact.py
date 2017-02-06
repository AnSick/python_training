from model.contact import Contact
from random import randrange
import random


def test_modify_some_contact_company(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test", last_name="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact = Contact(company="Peter-service")
    app.contact.modify_contact_by_id(contact.id, new_contact)
    new_contacts = db.get_contact_list()
    id = int(contact.id)
    for element in old_contacts:
        if element.id == id:
            element = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    def clean(contact):
        return Contact(id=contact.id, first_name=contact.first_name.strip(), last_name=contact.first_name.strip() )

    if check_ui:
        assert sorted(map(clean, new_contacts), key=Contact.id_or_max) == sorted(
            map(clean, app.contact.get_contact_list()), key=Contact.id_or_max)
