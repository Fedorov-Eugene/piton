from streams.console.input import Reader
from streams.console.output import Writer

class TypeForms(object):
	"""docstring for TypeForms"""
	def __init__(self):
		super(TypeForms, self).__init__()
		self.I = Reader()
		self.O = Writer()

	def request(self) -> str:
		return self.I.request()

	def write(self):
		self.O.response()

	def get_int(self):
		self.write("Enter Number: ")
		return int(self.request())

	def get_float(self):
		pass

	def get_complex(self):
		pass

	def get_str(self):
		pass

	def get_bool(self):
		pass