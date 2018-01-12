#Justin Moroz 11/17/2016 Section 002

name=input("Please enter your name: ")

name=name.replace(" ","")
name=name.lower()
print("Your name cleaned is: ",name)
number=0
for x in name:
    equivalent=(ord(x)-96)
    number+=equivalent
    print (equivalent)
print(number)

digit1=str(number)[-1]
digit2=str(number)[-2]
digit3=str(number)[-3]

all_numbers=int(digit1)+int(digit2)+int(digit3)
while all_numbers>9:
    digit1=str(all_numbers)[-1]
    digit2=str(all_numbers)[-2]
    all_numbers= int(digit1)+int(digit2)

print("Your name reduces to", all_numbers)

if all_numbers==1:
    print("This name means independence, loneliness, creativity, originality, dominance, leadership, impatience")
if all_numbers==2:
    print("This name means quiet, passive, diplomatic, co-operation, comforting, soothing, intuitive, compromising, patient")
if all_numbers==3:
    print("This name means charming, outgoing, self expressive, extroverted, abundance, active, energetic, proud")
if all_numbers==4:
    print("This name means harmony, truth, justice, order discipline, practicality")
if all_numbers==5:
    print("This name means new directions, excitement, change, adventure")
if all_numbers==6:
    print("This name means  love, harmony, perfection, marriage, tolerance, public service")
if all_numbers==7:
    print("This name means spirituality, completeness, isolation, introspection")
if all_numbers==8:
    print("This name means organization, business, commerce, new beginnings")
if all_numbers==9:
    print("This name means romantic, rebellious, determined, passionate, compassionate")
    
