class Command(object):
	"""docstring for Command"""
	def __init__(self, input_, output, func, prompts = "Enter: "):
		super(Command, self).__init__()
		self.In = input_
		self.Out = output
		self.action = func
		self.prompt = prompts

	def execute(self):
		if isinstance(self.In, str):
			self.Out(self.action(self.In))
		elif self.In == None:
			self.Out(self.action())
		else:
			self.Out(self.action(self.In(self.prompt)))

	def __call__(self):
		self.execute()