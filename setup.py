import views.console_input
import views.console_view

class Controller(object):
	"""Controller"""
	def __init__(self, input_, output):
		super(Controller, self).__init__()
		self.I = input_
		self.O = output

	def start():
		while True:
			print("1. Open TextStats module\n2. Open Sorting module\n3. Open UniqHolder module\n4. Exit")
			cmd = I.request("Enter command: ")
			if cmd == "1":
				pass
			elif cmd == "2":
				pass
			elif cmd == "3":
				pass
			else:
				break

def main():
	Controller(ConsoleReader(), ConsoleWriter()).start()

if __name__ == "__main__":
	main()