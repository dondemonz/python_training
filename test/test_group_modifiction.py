from model.group import Group

def test_group_name_modification(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="zzzz_11"))


"""
def test_group_header_modification(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(header="zzz_11"))
"""