class ConsoleReader(object):
	"""Can retrieve data fron console"""
	def __init__(self):
		super(ConsoleReader, self).__init__()

	def request(prompt):	
		return input(prompt)
		