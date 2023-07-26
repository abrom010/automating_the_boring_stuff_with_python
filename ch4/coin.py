import random
numberOfStreaks = 0
for experimentNumber in range(10000):
	# Code that creates a list of 100 'heads' or 'tails' values.
	tossList = []
	for i in range(100):
		tossList.append(random.randint(0,1))

	# Code that checks if there is a streak of 6 heads or tails in a row.
	count = 0
	heads = True
	for toss in tossList:
		if count == 6:
			numberOfStreaks += 1
			break
		if toss == 0:
			if heads == True:
				count += 1
			else:
				count = 0
				heads = False
		else:
			if heads == False:
				count += 1
			else:
				count = 0
				heads = True

print('Chance of streak: %s%%' % (numberOfStreaks / 100))