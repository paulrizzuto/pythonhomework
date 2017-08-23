import os
import re

newWords = []
totalLetters = 0

txtpath = os.path.join('..', '..', '08-01-2017-NB-Class-Repository-DATA', '02-HomeWork', '03-Python', 'Instructions', 'PyParagraph', 'raw_data', 'paragraph_2.txt')

with open(txtpath, 'r') as txtfile:
    filecontents = txtfile.read()

average = len(filecontents.split())/filecontents.count('.')    
    
with open(txtpath, 'r') as txtfile:    
    lines = txtfile.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            newWords.append(word)
    for item in newWords:
        totalLetters = totalLetters + len(item)

wordLength = totalLetters/len(newWords)

print("Paragraph Analysis")
print("-------------------------------------") 
print("Approximate Word Count: " + str(len(filecontents.split())))
print("Approximate Sentence Count: " + str(filecontents.count('.')))
print("Average Letter Count: " + str(round(wordLength, 2)))
print("Average Sentence Length: " + str(round(average, 2)))
