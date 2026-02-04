'''Generate unique usernames automatically.
Take full name from user
Convert to lowercase
Remove spaces
Add random 3-digit number
Store all usernames in a set (avoid duplicates)
Save all usernames into file
Example:Sachin Singh → sachinsingh452
Concepts used
string methods
set
random numbers
file handling
functions'''
import random
usernames=set()
def generate_username():
    name=input("Enter name to generate username:").lower()
    name=name.replace(" ","")
    number=random.randint(100,999)
    username=name+str(number)
    if username not in usernames:
        usernames.add(username)
        with open("user_name.txt","a") as file:
            file.write(username + "\n")
        print("Generated username=",username)
    else:
        print("Duplicate username try again..")
generate_username()
