import re
class UniqueHolder(object):
	"""Class which instances can hold multiple unique objects"""
	def __init__(self, args):
		super(UniqueHolder, self).__init__()
		self.holder = set(args)
	
	def add(self, first, *elements):
		self.holder |= (first | elements)

	def remove(self, element):
		self.holder -= element
	
	def find(self, first, *elements):
		return self.holder & (first | elements)	

	def list(self):
		return self.holder

	def grep(self, regex):
		reg = re.compile(regex)
		for var in self.holder:
			yield var if reg.match(var)

	def save(self, name):
		with open(name, "w") as file:
			file.writelines(self.holder)

	def load(self, name):
		with open(name, "r") as file:
			self.holder = file.readlines()
