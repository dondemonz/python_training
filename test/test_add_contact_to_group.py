from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture


def test_add_contact_to_group(app, db_orm):
    groups = db_orm.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name="987qwe", header="987qwe", footer="987qwe"))
    contacts = db_orm.get_contacts_list()
    if len(contacts) == 0:
        app.address.create(Contact(firstname="987qwe"))
    group_to_add = random.choice(groups)
    contact_to_add = random.choice(contacts)
    # добавляем контакт в группу
    app.contact.add_contact_to_group(contact_to_add.id, group_to_add.id)
    # print(contact_to_add)
    # print(group_to_add)
    # берем список контактов в нашей группе
    l = db_orm.get_contacts_in_group(Group(id=group_to_add.id))
    # проверяем, что наш id в этом списке.
    assert contact_to_add.id in app.contact.return_id_contacts(l), "Контакт не в группе"