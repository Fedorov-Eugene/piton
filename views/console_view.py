class ConsoleWriter(object):
	"""Can write data to console"""
	def __init__(self):
		super(ConsoleWriter, self).__init__()
		self.colors = {"red": '\033[91m', "yellow": '\033[93m', "green": '\033[92m', "blue": '\033[94m', "white": '\033[0m'}

	def response(text, flag = "white"):
		print(colors[flag] + text + colors["white"])		