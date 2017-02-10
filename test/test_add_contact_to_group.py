from model.contact import Contact
from model.group import Group
import random

def test_add_contact_to_group(app, orm):

    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    if (len(orm.get_contact_list()) == 0) or (len(orm.get_contacts_not_in_group(group)) ==0):
        app.contact.create(Contact(first_name="test", last_name="test"))
    contacts = orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    old_contacts = orm.get_contacts_in_group(group)
    app.contact.add_contact_to_group(int(contact.id), group.id)
    old_contacts.append(contact)
    new_contacts = orm.get_contacts_in_group(group)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)

