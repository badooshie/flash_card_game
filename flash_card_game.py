#! usr/bin/python3

"""
this is a script that will inpsect text from a formatted spanish list.

attempting to convert to classes per joe's recommendations.

TODO (from Joe):
 - convert to classes so it will organize into pretty chunks
 - presentToUser doesn’t use parameter “i”
 - Line under 63 converts int to int lol
 - all the int conversions... but I think you might able to have just 1 final int conversion, So wrap the whole thing I’m just one int
 - presentToUser uses “item” but it’s not passed in as a parameter. It works cuz it’s a global variable, but that’s usually not a great habit cuz it makes code confusing 


"""

import re
import random

fileLoc = '' # absolute file path to word list

correctList = []
notCorrectList = []
v1 = 0
v2 = 1

class card:
	def __init__(self,side1,side2):
		self.side1 = side1
		self.side2 = side2

class game:
	def __init__(self):
		pass

	def flashCardList():
		mainlist
		correctList
		incorrectList


	def checker(i):
		# checks right or wrong answer
		if i == True:
		correctList.append(i)
	else:
		notCorrectList.append(i)

def presentToUser(i):
	question = item[v1]
	answer = item[v2]
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
	v1,v2 = 1,0

while len(mo) > 0:
	item = random.sample(mo,1)[0]
	presentToUser(item)
	mo.remove(item)

correctScoreRatio = int(int(len(correctList))/int(fullListLength)*100)

# this is for testing
# print(correctList,notCorrectList)

print(f"You scored {correctScoreRatio}%")
