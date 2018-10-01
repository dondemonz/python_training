from model.group import Group

def test_group_modification(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="zzzz_11", header="zzz_11", footer="zzz_111"))
    app.session.logout()