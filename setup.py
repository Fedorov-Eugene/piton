import mathstats.search as se
import mathstats.sort as so
from views.console_input import ConsoleReader
from views.console_view	import ConsoleWriter

class Controller(object):
	"""Controller"""
	def __init__(self, input_, output):
		super(Controller, self).__init__()
		self.I = input_
		self.O = output

	def start(self):
		while True:
			print("\n1. Open TextStats module\n2. Open Sorting module\n3. Open UniqHolder module\n4. Exit")
			cmd = self.I.request("Enter command: ")
			if cmd == "1":
				se.main()
			elif cmd == "2":
				so.main()
			elif cmd == "3":
				pass
			else:
				break

def main():
	Controller(ConsoleReader(), ConsoleWriter()).start()

if __name__ == "__main__":
	main()