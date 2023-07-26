supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

# enumerate returns index and item
for index, item in enumerate(supplies):
	print('i: ' + str(index) + ' in supplies is: ' + item)

# multiple assignment
a, b, c, d = supplies

# in keyword
print('pens' in supplies)

# range really returns a sequence, like a list [0,1,2,3,4]
print(range(5))

import random

# random.choice randomly chooses item from list
print(random.choice(supplies))

# random.shuffle shuffles a list
random.shuffle(supplies)
print(supplies)

# the index method returns the index of item in list
print(supplies.index('flamethrowers'))

# list methods
supplies.append('scissors')
supplies.insert(3, 'notebooks')
supplies.remove('scissors')
supplies.sort()
supplies.reverse()
print(supplies)

# remember del also
del supplies[0]
print(supplies)

# The Python sequence data types include lists, strings, range objects, and tuples

# import copy
# copy.copy() copies a list
# copy.deepcopy() copies a list of lists