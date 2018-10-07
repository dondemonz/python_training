from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
     app.contact.create(Contact(firstname="123qwe", middlename="123qwe", lastname="123qwe", nickname="123qwe",
                       title="123qwe", image_path="C:\\1\\ArcheAge_sample.jpg", company="123qwe", address="123qwe", home="123qwe",
                       mobile="123qwe", work="123qwe", fax="123qwe", email="123qwe", email2="123qwe",
                       email3="123qwe", homepage="123qwe", bday="1", bmonth="January", byear="123q", aday="31",
                       amonth="December", ayear="9999", address2="123qwe", phone2="123qwe", notes="123qwe"))
    app.contact.delete_first_contact()


"""    
def test_delete_first_contact(app):
    # app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    # app.session.logout()
"""