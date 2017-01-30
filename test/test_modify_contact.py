from model.contact import Contact


def test_modify_first_contact_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    app.contact.modify_first_contact(Contact(company="Peter-service"))

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    #Edit contact by its identificator
    app.contact.edit_contact(2)
