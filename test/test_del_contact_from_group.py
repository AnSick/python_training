from model.contact import Contact
from model.group import Group
import random

def test_delete_contact_from_group(app, orm):
    if len(orm.get_groups_with_contacts())== 0:
        if len(orm.get_contact_list()) == 0:
            app.contact.create(Contact(first_name="test", last_name="test"))
        if len(orm.get_group_list()) == 0:
            app.group.create(Group(name="test"))
        contact = random.choice(orm.get_contact_list())
        group = random.choice(orm.get_group_list())
        app.contact.add_contact_to_group(int(contact.id), group.id)
    group = random.choice(orm.get_groups_with_contacts())
    old_contacts_in_group = orm.get_contacts_in_group(group)
    contact = random.choice(old_contacts_in_group)
    app.contact.delete_contact_from_group_by_index(contact.id, group.id)
    new_contacts = orm.get_contacts_in_group(group)
    old_contacts_in_group.remove(contact)
    assert sorted(old_contacts_in_group, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)