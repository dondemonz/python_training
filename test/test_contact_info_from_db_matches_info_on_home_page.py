from model.contact import Contact
import re


def test_contact_info_from_db_matches_info_on_home_page(app, db):
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname, lastname=contact.lastname,
                        address=contact.address, email=contact.email, email2=contact.email2, email3=contact.email3,
                        homephone=contact.homephone, workphone=contact.workphone, mobilephone=contact.mobilephone,
                       secondaryphone=contact.secondaryphone)
    ui_list = sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
    db_list = sorted(map(clean, db.get_contacts_list()), key=Contact.id_or_max)
    ui_phones_emails = []
    db_phones_emails = []
    for contact_db in db_list:
        all_phones_from_homepage = merge_phones_like_on_home_page(contact_db)
        all_emails_from_homepage = merge_emails_like_on_home_page(contact_db)
        ui_phones_emails.append(all_phones_from_homepage and all_emails_from_homepage)
    for contact_ui in ui_list:
        db_phones_emails.append(contact_ui.all_phones_from_home_page and contact_ui.all_emails)
    assert sorted(ui_phones_emails) == sorted(db_phones_emails)
    # print(ui_list)
    # print(db_list)
    assert ui_list == db_list


def clear(s):
    return re.sub("[() -]", "", s)



def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


