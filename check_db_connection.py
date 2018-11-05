from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


try:
    l = db.get_contacts_in_group(Group(id="69"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass   # db.destroy()



"""
try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
finally:
    db.destroy()
"""


"""
try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
"""