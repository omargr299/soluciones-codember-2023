from os import error
from urllib.request import urlopen
import re

data = urlopen("https://codember.dev/data/database_attacked.txt")
db = data.read().decode("utf-8")
rows = db.split("\n")
email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
location_regex = re.compile(r"[A-Z\b]")

def evaluate_user(user):
    id,user_name,email,age,location = user.split(",")

    if len(id) < 1 or not id.isalnum():
        return False

    if len(user_name) < 1 or not user_name.isalnum():
        return False

    
    if len(email) < 1 or  email_regex.search(email) == None:
        return False

    if len(age) > 1 and not age.isnumeric():
        return False

    
    if len(location) > 0 and location_regex.search(location) == None :
        return False
    
    return True

invalid_users = []
for row in rows:
   
   if not evaluate_user(row):
        user_name = row.split(",")[1]
        invalid_users.append(user_name[0])
        
print("".join(invalid_users))
        
    