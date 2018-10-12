# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="123qwe", middlename="123qwe", lastname="123qwe", nickname="123qwe",
                       title="123qwe", image_path="C:\\1\\ArcheAge_sample.jpg", company="123qwe", address="123qwe", home="123qwe",
                       mobile="123qwe", work="123qwe", fax="123qwe", email="123qwe", email2="123qwe",
                       email3="123qwe", homepage="123qwe", bday="1", bmonth="January", byear="123q", aday="31",
                       amonth="December", ayear="9999", address2="123qwe", phone2="123qwe", notes="123qwe")
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
def test_add_empty_contact(self):
    wd = self.wd
    self.open_home_page(wd)
    self.login(wd, username="admin", password="secret")
    self.create_contact(wd, Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                        address="", home="",
                                        mobile="", work="", fax="", email="", email2="", email3="", homepage="",
                                        byear="", ayear="",
                                        address2="", phone2="", notes="", image_path=""))
    self.return_to_home_page(wd)
    self.wd.implicitly_wait(30)
    self.logout(wd)
"""

