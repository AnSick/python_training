from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    #Удаление группы по ее идентификатору в базе данных
    app.group.delete_group(18)