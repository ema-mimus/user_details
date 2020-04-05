import random
import string

def randomString(stringLength):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def getDetails():
    firstname = input("Please enter your first name: ")
    lastname = input("Please enter your last name: ")
    email = input("What is your email address: ")
    name = firstname + " " + lastname

    password = firstname[0:2] + lastname[-2:] + randomString(5)
    print("Your password is " + password)

    choice = input("Please type Yes if happy with password otherwise press enter to choose new password")
    if choice == "Yes":
        print("Your name is " + name + "." + "Your email is " + email + "." + "Your password is " + password)
    else:
        userpass = input("Choose your password")
        while len(userpass) < 7:
            print("Password must be up to 7 characters")
            userpass = input("Choose your password")
        else:
            print("Your name is " + name + "." + "Your email is " + email + "." + "Your password is " + userpass)
            
    details = [firstname, lastname, email]
    return details
        
status = True
container = []
while status:
    details = getDetails()
    container.append(details)
    
    newUser = input("Would you like to enter a new user? Yes or No")
    if (newUser == "No"):
        status = False
        for item in container:
            print(item)
            
    else:
        status = True