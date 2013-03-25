class Hero(object):
	"""docstring for Hero"""
	def __init__(self, max_hp, hp, max_mp, mp, strength, defence, level, armour):
		self.level = level
		self.max_hp = max_hp
		self.max_mp = max_mp 
		self.armour = armour
		self.defence = defence
		self.strength = strength	

	def Level(level, current_xp):
		if current_xp >= level * 100:
			level += 1
		else:
			pass


class Knight(Hero):

	def __init__(self):
		max_hp = 150
		hp = max_hp
		max_mp = 20
		mp = max_mp
		level = 1
		armour = 0

	@property 
	def defence(self):
	 		return 3 * self.level * self.armour

	@property 
	def strength(self):
		return 4 * self.level + self.max_hp










