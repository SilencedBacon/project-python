from pprint import pprint

#creates a list
inv = []

inv.append('Lesser Healing Potion')
# creates a dictionary, item name is the key to access values. To be appended to player's inventory through function
# hp+, mp+, sell price
itemvalues = {	'Lesser Healing Potion':[100,0,10],
				'Greater Healing Potion':[250,0,50],
				'Superior Healing Potion':[500,0,100],
				'Lesser Mana Potion':[0,25,10],
				'Greater Mana Potion':[50,50,50],
				'Superior Mana Potion':[50,100,100],
				'Restoration Potion':[250,50,250],
				'Gold Nugget':[0,0,500]

}
print itemvalues
print inv 
inv.append('Greater Healing Potion')
print inv
# extend appens multiple values
inv.extend(itemvalues)

def inspect_inv():
	pprint(itemvalues)

# def use_item():


# inspect_inv()

# if 'Lesser Healing Potion' in itemvalues:
# 	print itemvalues['Lesser Healing Potion']
# else:
# 	print 'Not Found'

print itemvalues.get('Gold Nugget', 500)
# retrieves a specific value from a dictionary itemvalues
a = itemvalues.get('Gold Nugget')[2:]
print a
# how to do maths with list items, use for healing and game economy
b = [5+x for x in a]
print b

