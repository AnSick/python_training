from model.group import Group
from random import randrange
import random

def test_modify_some_group_name(db, app, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New group"))
    new_group = Group(name="test")
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    id = int(group.id)
    #old_groups[] = new_group
    for element in old_groups:
        if element.id == id:
            element = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    if check_ui:
        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(
            map(clean, app.group.get_group_list()), key=Group.id_or_max)

