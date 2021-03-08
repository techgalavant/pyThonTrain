name = input('What is your name?\n')
print('Hi, %s.' % name)
from replit import db
db["name"]= (name)
keys = db.keys()
matches = db.prefix("n")
print (matches)
value = db["name"]
print (value)