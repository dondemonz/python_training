from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="9_z", middlename="9_z", lastname="9_z", nickname="9_z",
                       title="9_z", image_path="C:\\1\\ArcheAge_sample.jpg", company="9_z", address="9_z", home="9_z",
                       mobile="9_z", work="9_z", fax="9_z", email="9_z", email2="9_z",
                       email3="9_z", homepage="9_z", bday="30", bmonth="December", byear="9_z", aday="1", amonth="April",
                       ayear="0__2", address2="9_z", phone2="9_z", notes="9_z"))
    app.session.logout()