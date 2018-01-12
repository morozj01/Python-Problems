#Justin Moroz Section 002 12/15/2016

thesaurus={
    "happy":"glad",
    "sad":"bleak",
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
            index=phrase.index(x)
            phrase.remove(x)
            phrase.insert(index,replacement.upper())

newstring=' '.join(phrase)
print(newstring)


