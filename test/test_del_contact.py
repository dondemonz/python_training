from model.contact import Contact
import random
import time

def test_delete_some_contact(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname="123qwe", lastname="123qwe"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(2)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

"""    


 app.contact.create(Contact(firstname="123qwe", middlename="123qwe", lastname="123qwe", nickname="123qwe",
                       title="123qwe", image_path="C:\\1\\ArcheAge_sample.jpg", company="123qwe", address="123qwe", home="123qwe",
                       mobile="123qwe", work="123qwe", fax="123qwe", email="123qwe", email2="123qwe",
                       email3="123qwe", homepage="123qwe", bday="1", bmonth="January", byear="123q", aday="31",
                       amonth="December", ayear="9999", address2="123qwe", phone2="123qwe", notes="123qwe"))



"""