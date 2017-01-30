from model.contact import Contact


def test_modify_first_contact_company(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(company="Peter-service"))
    app.session.logout()

def test_edit_contact(app):
    #Edit contact by its identificator
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(2)
    app.session.logout()
