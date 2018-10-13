from model.contact import Contact
from random import randrange

def test_contact_modification(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="123qwe", lastname="123qwe"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="9_z", lastname="9_z")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    """
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="123qwe", middlename="123qwe", lastname="123qwe", nickname="123qwe",
                                   title="123qwe", image_path="C:\\1\\ArcheAge_sample.jpg", company="123qwe",
                                   address="123qwe", home="123qwe",
                                   mobile="123qwe", work="123qwe", fax="123qwe", email="123qwe", email2="123qwe",
                                   email3="123qwe", homepage="123qwe", bday="1", bmonth="January", byear="123q",
                                   aday="31",
                                   amonth="December", ayear="9999", address2="123qwe", phone2="123qwe", notes="123qwe"))
    """