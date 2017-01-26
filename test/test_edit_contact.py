def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact()
    app.session.logout()

def test_edit_contact(app):
    #Edit contact by its identificator
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(2)
    app.session.logout()
