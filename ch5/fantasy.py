stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
	print("Inventory:")
	item_total = 0
	for k,v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v
	print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
	for item in addedItems:
		inventory[item] = inventory.get(item, 0) + 1

displayInventory(stuff)
dragonLoot = ['gold coin', 'dagger', 'ruby', 'gold coin']
addToInventory(stuff, dragonLoot)
displayInventory(stuff)