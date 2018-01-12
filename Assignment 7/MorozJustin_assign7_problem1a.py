#Justin Moroz 11/17/2016 Section 002

user=input("Pleae enter a username: ")
accept=False
while accept==False:
    if len(user)>15 or len(user)<8:
        print("Username must be between 8 and 15 characters")
        user=input("Please enter another user name: ")
    if user.isalnum()==False:
        print("Username can only contain letters and numbers")
        user=input("Please enter another username")
    if user.isupper()==True:
        print("Username must contain at least one lowercase letter")
        user=input("Please enter another username")
    if user.islower()==True:
        print("Username must contain at least one uppercase letter")
        user=input("Please enter another username")
    if user.isalpha()==True:
        print("Username must contain at least one number")
        user=input("Please enter another username")
    if user[0].isnumeric() or user[-1].isnumeric==True:
        print("Username cannot have a number as the first or last character")
        user=input("Please enter another username")
    else:
        print("Uername is valid")
        break
