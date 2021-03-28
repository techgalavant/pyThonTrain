from replit import db

name = input('What is your name?\n')
street = input('What is the name of your street?\n')
number = input('Telephone number?\n')


def db_test():
    db["key1"] = name
    db["key2"] = street
    db["number"] = number
    keys = db.keys()
    matches = db.prefix("n")
    print(matches)
    value = db["name"]
    print(value)
    value2 = db["number"]
    print(value2)


if __name__ == '__main__':
    db_test()
# https://pypi.org/project/firebase/
# https://firebase.googleblog.com/2017/07/accessing-database-from-python-admin-sdk.html
