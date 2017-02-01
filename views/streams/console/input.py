class Reader(object):
	"""Can retrieve data fron console"""
	def __init__(self, prompt="": str):
		super(ConsoleReader, self).__init__()
		self.prompt = prompt

	def request(self) -> str:
		return input(self.prompt)

		