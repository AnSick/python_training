def test_delete_first_group(app):
    app.group.delete_first_group()


def test_delete_group(app):
    #Удаление группы по ее идентификатору в базе данных
    app.group.delete_group(18)