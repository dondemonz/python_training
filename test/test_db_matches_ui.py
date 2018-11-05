from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture

import re

def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=re.sub(' +', ' ', group.name.strip()))
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

def test_contacts_list(app, db_orm):
    ui_list = app.contact.get_contacts_list()
    db_list = db_orm.get_contacts_list()
    # print(sorted(ui_list, key=Contact.id_or_max))
    # print(sorted(db_list, key=Contact.id_or_max))
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)