#Justin Moroz Section 002 12/15/2016
import random
thesaurus={
    "happy":["glad","blissful","estatic","at ease"],
    "sad":["bleak","blue","depressed"]
    }
words=input("Please enter a phrase: ")
clean_word=words.replace('!',"")
clean_word=clean_word.replace('?',"")
clean_word=clean_word.replace('.',"")
clean_word=clean_word.replace(',',"")
phrase=clean_word.split(" ")
keys=thesaurus.keys()
print(clean_word)


for x in phrase:
    for y in keys:
        if x==y:
            replacement=thesaurus.get(y)
            random_index=random.randint(0,len(replacement))
            replacement_string=replacement[random_index]
            index=phrase.index(x)
            phrase.remove(x)
            phrase.insert(index,replacement_string.upper())

newstring=' '.join(phrase)
print(newstring)
