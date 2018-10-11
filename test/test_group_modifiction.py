from model.group import Group

def test_group_name_modification(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="zzzz_11"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


"""
def test_group_header_modification(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="zzz_11"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

"""