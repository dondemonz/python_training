from model.contact import Contact


testdata = [
    Contact(firstname="firstname1", lastname="lastname1", middlename="middlename1"),
    Contact(firstname="firstname2", lastname="lastname2", middlename="middlename2"),
]



""" генератор случайных значений
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", middlename="")] + [
    Contact(firstname=random_string("firstname", 5), lastname=random_string("lastname", 10), middlename=random_string("middlename", 15))
    for i in range(5)
]

"""