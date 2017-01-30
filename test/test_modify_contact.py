from model.contact import Contact


def test_modify_first_contact_company(app):
    app.contact.modify_first_contact(Contact(company="Peter-service"))

def test_edit_contact(app):
    #Edit contact by its identificator
    app.contact.edit_contact(2)
