# -*- coding: utf-8 -*-
from model.group import Group
import time


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    time.sleep(2)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)






# хеширование, полсчет элементов в пользовательском интерфейсе
# assert len(old_groups) + 1 == app.group.count()