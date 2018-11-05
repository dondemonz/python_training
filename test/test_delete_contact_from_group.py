from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

def test_delete_contact_from_group(app, db_orm):
    contacts = db_orm.get_contacts_list()
    if len(contacts) == 0:
        app.contact.create(Contact(firstname="qwe123"))
    groups = db_orm.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name="qwe123", header="qwe123", footer="qwe123"))
    groups = db_orm.get_group_list()
    # проверяем, есть ли контакты в группах?
    group_id = None
    for row in groups:
        if len(db_orm.get_contacts_in_group(Group(id=row.id))) > 0:
            group_id = row.id
            break
    # если контактов нет, то добавляем
    if group_id == None:
        group_to_add = random.choice(groups)
        contact_to_add = random.choice(contacts)
        app.contact.add_contact_to_group(contact_to_add.id, group_to_add.id)
        group_id = group_to_add.id
    # удаляем первый элемент привязанный к группе
    # app.contact.return_to_home_page()
    id_contact = app.contact.delete_contact_from_group(group_id)
    # проверяем список контактов, которые не в этой группе
    l = db_orm.get_contacts_not_in_group(Group(id=group_id))
    assert id_contact in app.contact.return_id_contacts(l), "Ошибка, контакт в группе"
