import re
class UniqueHolder(object):
	"""Class which instances can hold multiple unique objects"""
	def __init__(self, args = []):
		super(UniqueHolder, self).__init__()
		self.holder = set(args)
	
	def add(self, first):
		self.holder |= set(first)

	def remove(self, element):
		self.holder -= set(element)
	
	def find(self, first):
		return self.holder & set(first)

	def list(self):
		return self.holder

	def grep(self, regex):
		reg = re.compile(regex)
		for var in self.holder:
			if re.match(reg, var):
				yield var

	def save(self, name):
		with open(name, "w+") as file:
			file.writelines(self.holder)

	def load(self, name):
		with open(name, "r+") as file:
			self.holder = set(file.readlines())
