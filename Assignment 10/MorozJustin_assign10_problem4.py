#Justin Moroz Section 002 12/15/2016
import random
import urllib.request
thesaurus={}
data=urllib.request.urlopen('http://cs.nyu.edu/~abrahamr/courses/cs0002spring2016/thesaurus.txt')
wordlist=data.read().decode('utf-8')


condensed=wordlist.split('\n')
for x in condensed:
    single_words=x.split(",")
    count=0
    for y in single_words:
        if len(single_words)>1:
            thesaurus[single_words[0]]=single_words[count]
            count+=1
        else:
            thesaurus[single_words[0]]=""

data2=urllib.request.urlopen('http://cs.nyu.edu/~abrahamr/courses/cs0002spring2016/bieber_baby.txt')
words=data2.read().decode('utf-8')
clean_word=words.replace('!',"")
clean_word=clean_word.replace('?',"")
clean_word=clean_word.replace('.',"")
clean_word=clean_word.replace(',',"")

list1=clean_word.split(" ")
keys=thesaurus.keys()



for x in phrase:
    for y in keys:
        replace=random.randint(
        if x==y:
            replacement=thesaurus.get(y)
            random_index=random.randint(0,len(replacement))
            replacement_string=replacement[random_index]
            index=phrase.index(x)
            phrase.remove(x)
            phrase.insert(index,replacement_string.upper())

newstring=' '.join(phrase)
print(newstring)
