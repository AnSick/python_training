def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group()
    app.session.logout()

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(16)
    app.session.logout()