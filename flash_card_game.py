#! usr/bin/python3

"""
this is a script that will inpsect text from a formatted spanish list.

it will see all the pairs making a dictionary. it will then randomize that dictionary and offer each word to the user until each word has been seen once.

the word presented will be in spanish allowing the user to check if they can remember by typing in the english word.

the program will then check it against the dictionary value and return correct if it is the same or incorrect if it is not.

the corrects and incorrects will be saved to a list that will show a percentage of right to wrong.



"""

import re
import random

fileLoc = '' # absolute file path to word list

correctList = []
notCorrectList = []
wordPos = 0
definitionPos = 1

def listChooser(i):
	if i == True:
		correctList.append(i)
	else:
		notCorrectList.append(i)

def presentToUser(i):
	question = i[wordPos]
	answer = i[definitionPos]
	print(question)
	userAnswer = input()
	score = userAnswer == answer
	print(score)
	listChooser(score)

with open(fileLoc, encoding='UTF-8') as f:
	contents = f.read()

m = re.compile(r'Word: (.*)\nDefinition: (.*)')
mo = set(m.findall(contents))

fullListLength = len(mo)
print(fullListLength)

flashSwitch = input("s or e: ")
if flashSwitch == "s":
	pass
else:
	wordPos,definitionPos = 1,0

while len(mo) > 0:
	item = random.sample(mo,1)[0]
	presentToUser(item)
	mo.remove(item)

correctScoreRatio = int(int(len(correctList))/int(fullListLength)*100)

# this is for testing
# print(correctList,notCorrectList)

print(f"You scored {correctScoreRatio}%")
