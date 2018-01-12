#MorozJustin 12/4/2016 Section 002

def listlen(alist):
    length=0
    for x in alist:
        length+=1
    return length
    print(length)



def listmax(alist):
    counter=0
    if listlen(alist)==0:
        return "NONE"
    else:
        maxnum=alist[0]
        for x in alist:
            if maxnum<x:
                maxnum=x
        return maxnum

def listcopy(alist):
    newlist=alist
    return newlist


def listappend(alist,data):
    str1=str(alist).strip('[]')
    str1=str1+","
    str1=str1+str(data)
    newlist=str1.split(',')
    return newlist

def listinsert(alist,location,data):
    str1=str(alist[:location:]).strip('[]')
    str2=","+str(alist[location::]).strip('[]')
    str1=str1+","
    str1=str1+str(data)
    fullstring=str1+str2
    newlist=fullstring.split(',')
    return newlist

def listremove(alist,data):
    str1=str(alist).strip('[]')
    data1=str(data)+','
    data2="'"+str(data)+"'"
    new_string=str1.replace(data1,'')
    new_string=str1.replace(data2,'')
    newlist=new_string.split(',')
    return newlist

def listreverse(alist):
    str1=''
    for x in alist[::-1]:
        str1=str1+str(x)
        str1=str1+','
    newlist=str1.split(',')
    return newlist



    
