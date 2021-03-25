name = input('What is your name?\n')
street = input('What is the name of your street?\n')
number = input('Telephone number?\n')

from replit import db

db["name"] = name
db["street"] = (street)
db["number"] = (number)
keys = db.keys()
matches = db.prefix("n")
print(matches)
value = db["name"]
print(value)
value2 = db["number"]
print(value2)
## https://pypi.org/project/firebase/
## https://firebase.googleblog.com/2017/07/accessing-database-from-python-admin-sdk.html
