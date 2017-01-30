class ConsoleWriter(object):
	"""Can write data to console"""
	colors = {"red": '\033[91m', "yellow": '\033[93m', "green": '\033[92m', "blue": '\033[94m', "white": '\033[0m'}

	def response(self, text, flag = "white"):
		print(self.colors[flag]+ text + self.colors["white"] )		