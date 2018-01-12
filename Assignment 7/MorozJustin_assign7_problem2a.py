#Justin Moroz 11/17/2016 Section 002

name=input("Please enter your name: ")

name=name.replace(" ","")
name=name.lower()
number=0
for x in name:
    equivalent=(ord(x)-96)
    number+=equivalent
    print (equivalent)
print(number)
