from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        """
        self.middlename = middlename
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.image_path = image_path
        self.bday = bday
        self.bmonth = bmonth
        self.aday = aday
        self.amonth = amonth
        """
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize