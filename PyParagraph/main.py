import os
import re

newWords = []
newSentences = []
totalLetters = 0
sentenceLength = []
averageSentence = 0

txtpath = os.path.join('..', '..', '..', '08-01-2017-NB-Class-Repository-DATA', '02-HomeWork', '03-Python', 'Instructions', 'PyParagraph', 'raw_data', 'paragraph_2.txt')

with open(txtpath, 'r') as txtfile:
    lines = txtfile.readlines()
    sentences = re.split("(?<=[.!?]) +", txtfile)

    for line in lines:
        words = line.split()
        
        for word in words:
            newWords.append(word)

        # for sentence in sentences:
        #     newSentences.append(sentence)

    for item in newWords:
        totalLetters = totalLetters + len(item)

    # for item in newSentences:
    #     length = 0
    #     words = item.split()
    #     for word in words:
    #         length = length + 1
    #     sentenceLength.append(length)
    
# for item in range(len(sentenceLength)):
#     averageSentence = averageSentence + sentenceLength[item]

# average = averageSentence/(len(sentenceLength)-1)

wordLength = totalLetters/len(newWords)

print(sentences)

print("Paragraph Analysis")
print("-------------------------------------") 
print("Approximate Word Count: " + str(len(newWords)))
# print("Approximate Sentence Count: " + str(len(newSentences)-1))
print("Average Letter Count: " + str(round(wordLength, 2)))
# print("Average Sentence Length: " + str(round(average, 2)))
