from model.group import Group

def test_group_name_modification(app):
    app.group.modify_first_group(Group(name="zzzz_11"))


def test_group_header_modification(app):
    app.group.modify_first_group(Group(header="zzz_11"))


