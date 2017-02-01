class Writer(object):
	"""docstring for FileWriter"""
	def __init__(self, file):
		super(FileWriter, self).__init__()
		self.name = file

	def response(self, data) -> None:
		with open(self.name, "w+") as file:
			raise NotImplementedException()

		