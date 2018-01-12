#MorozJustin 11/28/2016 Section 002
#Prompt user for their number
length=int(input("Enter a positive integer greater then 10: "))
#Validate their input
while length<10:
    length=int(input("Must be a positive integer greater then 10: "))
#Create the original list of numbers, 1 and 2 are designated not prime
#All other numbers are assumed to be prime
numbers= ["N","N"]+["P"]*(length-1)

#alter the list and change all non-prime numbers to "N" using a nested for loop
for x in range(2,length+1):
    for y in range (x+1, length+1):
        if y%x==0:
            numbers[y]="N"
#iterate through the new list and print all instances of "P"        
counter=0
prime=0
for x in numbers:
    if x=="P":
        counter=str(counter)
        print(counter, end=" "*(7-len(counter)))
        prime+=1
        counter=int(counter)
        if prime%10==0:
            print("\n")
    counter+=1






   
    
