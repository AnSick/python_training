def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()


def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_contact(25)
    app.session.logout()
