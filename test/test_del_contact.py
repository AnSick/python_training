def test_delete_first_contact(app):
    app.contact.delete_first_contact()


def test_delete_contact(app):
    app.contact.delete_contact(25)