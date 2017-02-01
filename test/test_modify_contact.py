from model.contact import Contact


def test_modify_first_contact_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(company="Peter-service")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_edit_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first_name="test"))
#    old_contacts = app.contact.get_contact_list()
#    #Edit contact by its identificator
#    app.contact.edit_contact(2)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
