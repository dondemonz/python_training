from model.contact import Contact

def test_contact_modification(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="123qwe", middlename="123qwe", lastname="123qwe", nickname="123qwe",
                                   title="123qwe", image_path="C:\\1\\ArcheAge_sample.jpg", company="123qwe",
                                   address="123qwe", home="123qwe",
                                   mobile="123qwe", work="123qwe", fax="123qwe", email="123qwe", email2="123qwe",
                                   email3="123qwe", homepage="123qwe", bday="1", bmonth="January", byear="123q",
                                   aday="31",
                                   amonth="December", ayear="9999", address2="123qwe", phone2="123qwe", notes="123qwe"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.modify_first_contact(Contact(firstname="9_z", middlename="9_z", lastname="9_z", nickname="9_z",
                       title="9_z", image_path="C:\\1\\ArcheAge_sample.jpg", company="9_z", address="9_z", home="9_z",
                       mobile="9_z", work="9_z", fax="9_z", email="9_z", email2="9_z",
                       email3="9_z", homepage="9_z", bday="30", bmonth="December", byear="9_z", aday="1", amonth="April",
                       ayear="0__2", address2="9_z", phone2="9_z", notes="9_z"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
