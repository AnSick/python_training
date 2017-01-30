from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    app.contact.delete_first_contact()


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    app.contact.delete_contact(25)