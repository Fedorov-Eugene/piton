from streams.console.input import Reader
from streams.console.output import Writer

class TypeTemplates(object):
	"""docstring for TypeTemplates"""
	def __init__(self, arg):
		super(TypeTemplates, self).__init__()
		self.I = Reader()
		self.O = Writer()

	def write(self):
		self.O.response()

	def request(self):
		return self.I.request()
	
	def confirm(self, yes="Y", no="n", default=False):
		self.write("Are you sure? [%s/%s]: " % (yes, no))
		options = {yes: True, no: False}
		decision = self.request()
		return options[decision] if decision in options else default
