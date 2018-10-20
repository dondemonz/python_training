# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", middlename="")] + [
    Contact(firstname=random_string("firstname", 5), lastname=random_string("lastname", 10), middlename=random_string("middlename", 15))
    for i in range(5)
]



@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


"""
contact = Contact(firstname="123qwe", middlename="123qwe", lastname="123qwe", nickname="123qwe",
                       title="123qwe", image_path="C:\\1\\ArcheAge_sample.jpg", company="123qwe", address="123qwe", home="123qwe",
                       mobile="123qwe", work="123qwe", fax="123qwe", email="123qwe", email2="123qwe",
                       email3="123qwe", homepage="123qwe", bday="1", bmonth="January", byear="123q", aday="31",
                       amonth="December", ayear="9999", address2="123qwe", phone2="123qwe", notes="123qwe")
"""

"""
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, contact):
    old_groups = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,  key=Contact.id_or_max)



contact = Contact(firstname="123qwe", lastname="123qwe")
"""


