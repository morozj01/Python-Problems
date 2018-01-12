#Justin Moroz 11/28/2016 Section 002

test1= int(input("Please enter the first test score (10-100): "))
while test1>100 or test1<10:
    test1=int(input("That isnt valid. Please enter a different score: "))

test2= int(input("Please enter the second test score: "))
while test2>100 or test2<10:
    test2=int(input("That isnt valid. Please enter a different score: "))
                
test3= int(input("Please enter the third test score: "))
while test3>100 or test3<10:
    test3=int(input("That isnt valid. Please enter a different score: "))
                
test4= int(input("Please enter the fourth test score: "))
while test4>100 or test4<10:
    test4=int(input("That isnt valid. Please enter a different score: "))
                 
test5= int(input("Please enter the fifth test score: "))
while test5>100 or test5<10:
    test5=int(input("That isnt valid. Please enter a different score: "))
                
scores=[test1,test2,test3,test4,test5]

average=(test1+test2+test3+test4+test5)/5
highest=max(scores)
lowest=min(scores)

print("Here are your scores:")
print(scores)
print("Average is:",average)
print("Highest score is:", highest)
print("Lowest score is:", lowest)

willcurve=input("Do you want to curve the scores? (yes/no): ")
if willcurve=="yes":
    curve=int(input("How big will the curve be: "))

counter=0
while counter<5:
    scores[counter]+=curve
    counter+=1
averagec=(scores[0]+scores[1]+scores[2]+scores[3]+scores[4])/5
highestc=max(scores)
lowestc=min(scores)

print("Your new scores are:")
print(scores)
print("Average is:", averagec)
print("Highest scores is:", highestc)
print("Lowest score is:", lowestc)


          
