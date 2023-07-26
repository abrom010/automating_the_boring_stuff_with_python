tableData = [['apples', 'oranges', 'cherries', 'banana'],
			['Alice', 'Bob', 'Carol', 'David'],
			['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
	maxList = []
	for row in tableData:
		max = 0
		for item in row:
			if len(item) > max:
				max = len(item)
		maxList.append(max)

	count = 0
	for j in range(len(tableData[0])):
		for i in range(len(tableData)):
			print(tableData[i][j].rjust(maxList[i]) + ' ', end="")
			count += 1
			if count == len(tableData[0]) - 1:
				print()
				count = 0

printTable(tableData)

