# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    def clean(contact):
        return Contact(id=contact.id, first_name=contact.first_name.strip(), last_name=contact.first_name.strip() )

    if check_ui:
        assert sorted(map(clean, new_contacts), key=Contact.id_or_max) == sorted(
            map(clean, app.contact.get_contact_list()), key=Contact.id_or_max)
