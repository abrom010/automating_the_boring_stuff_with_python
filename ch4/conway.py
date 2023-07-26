# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells
nextCells = []
for x in range(WIDTH):
	column = []
	for y in range(HEIGHT):
		if random.randint(0,1) == 0:
			column.append('#') # Add a living cell
		else:
			column.append(' ') # Add a dead cell
	nextCells.append(column) # nextCells is a list of column lists

while True:
	print('\n\n\n\n\n') # separate each step
	currentCells = copy.deepcopy(nextCells)

	# Print currentCells
	for y in range(HEIGHT):
		for x in range(WIDTH):
			print(currentCells[x][y], end='') # Print # or space
		print()

	# Calculate the next step's cells based on current step's cells
	for x in range(WIDTH):
		for y in range(HEIGHT):
			# get neighboring coords
			# '% WIDTH' ensures leftcoord is always between 0 and WIDTH - 1
			leftCoord = (x-1) % WIDTH
			rightCoord = (x+1) % WIDTH
			aboveCoord = (y-1) % HEIGHT
			belowCoord = (y+1) % HEIGHT

			# count number of living neighbors
			numNeighbors = 0
			if currentCells[leftCoord][aboveCoord] == '#':
				numNeighbors += 1 # top-left is alive
			if currentCells[x][aboveCoord] == '#':
				numNeighbors == 1 # top alive
			if currentCells[rightCoord][aboveCoord] == '#':
				numNeighbors += 1 # top-right alive
			if currentCells[leftCoord][y] == '#':
				numNeighbors += 1 # left alive
			if currentCells[rightCoord][y] == '#':
				numNeighbors += 1 # right alive
			if currentCells[leftCoord][belowCoord] == '#':
				numNeighbors += 1 # bottom-left alive
			if currentCells[x][belowCoord] == '#':
				numNeighbors += 1 # bottom alive
			if currentCells[rightCoord][belowCoord] == '#':
				numNeighbors += 1 # bottom-right alive

			# Set cell based on Conway's Game of Life rules
			if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
				# Living cells with 2 or 3 neighbors stay alive
				nextCells[x][y] = '#'
			elif currentCells[x][y] == ' ' and numNeighbors == 3:
				# Dead cells with 3 neighbors become alive
				nextCells[x][y] = '#'
			else:
				# Everything else dies or stays dead
				nextCells[x][y] = ' '

	time.sleep(1)