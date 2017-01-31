from model.contact import Contact


def test_modify_first_contact_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(company="Peter-service"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    old_contacts = app.contact.get_contact_list()
    #Edit contact by its identificator
    app.contact.edit_contact(2)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
