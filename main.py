name = input('What is your name?\n')
from replit import db

db["name"]= (name)
keys = db.keys()
matches = db.prefix("n")
print (matches)
value = db["name"]
print (value)
## https://pypi.org/project/firebase/
## https://firebase.googleblog.com/2017/07/accessing-database-from-python-admin-sdk.html
