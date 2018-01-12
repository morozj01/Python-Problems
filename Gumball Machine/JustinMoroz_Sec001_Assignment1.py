#Justin Moroz      1/27/2017

import random
#create list called gumballs
gumballs=[]

#append appropriate amount into list for each color
yellow=random.randint(10,15)
count=0
while count<yellow:
    gumballs.append("yellow")
    count+=1

blue=random.randint(1,10)
count=0
while count<blue:
    gumballs.append("blue")
    count+=1

white=random.randint(6,15)
count=0
while count<blue:
    gumballs.append("blue")
    count+=1

green=random.randint(10,25)
count=0
while count<blue:
    gumballs.append("green")
    count+=1

black=random.randint(1,12)
count=0
while count<blue:
    gumballs.append("black")
    count+=1

purple=random.randint(5,10)
count=0
while count<purple:
    gumballs.append("purple")
    count+=1

silver=random.randint(4,6)
count=0
while count<silver:
    gumballs.append("silver")
    count+=1

cyan=random.randint(5,12)
count=0
while count<blue:
    gumballs.append("cyan")
    count+=1

magenta=random.randint(0,10)
count=0
while count<blue:
    gumballs.append("blue")
    count+=1

gumballs.append("red")

#display gumball count
print("You are starting with the following gumballs:")
print(yellow,"yellow")
print(blue,"blue")
print(white,"white")
print(green,"green")
print(black,"black")
print(purple,"purple")
print(silver,"silver")
print(cyan,"cyan")
print(magenta,"magenta")
print("and 1 red")
print()
print("Here are your random purchases:")

#begin drawing at random
draw=""
taken=[]
tracker=0
while draw!="red":
    draw_num=random.randint(0,(len(gumballs)-1))
    draw=gumballs[draw_num]
    gumballs.remove(draw)
    taken.append(draw)
    tracker+=1
    print(draw)

#determine most common gumball drawn
import collections
countlist={"yellow":[],"blue":[],"white":[],"green":[],"black":[],"purple":[],"silver":[],"cyan":[],"magenta":[],"red":[]}

yellow_count=taken.count("yellow")
countlist["yellow"].append(yellow_count)

blue_count=taken.count("blue")
countlist["blue"].append(blue_count)

white_count=taken.count("white")
countlist["white"].append(white_count)

green_count=taken.count("green")
countlist["green"].append(green_count)

black_count=taken.count("black")
countlist["black"].append(black_count)

purple_count=taken.count("purple")
countlist["purple"].append(purple_count)

silver_count=taken.count("silver")
countlist["silver"].append(silver_count)

cyan_count=taken.count("cyan")
countlist["cyan"].append(cyan_count)

magenta_count=taken.count("magenta")
countlist["magenta"].append(magenta_count)

countlist=collections.Counter(countlist)
most=countlist.most_common(1)
most=str(most[0])
most=most.replace("(","")
most=most.replace("'","")
most=most.replace(")","")
most=most.replace("[","")
most=most.replace("]","")
most=most.split(",")

print()
print("You purchased",tracker,"gumballs for a price of $",(tracker*.25))
print("The most common color gumball you recieved was",most[0], "which you received",most[1],"times")



    




    



    
