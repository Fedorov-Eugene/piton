import mathstats.search as se
import mathstats.sort as so
from views.console_input import ConsoleReader
from views.console_view import ConsoleWriter

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
                se.main(self.get_date('path of text file'))
            elif cmd == "2":
                so.main(self.get_date('path of numbre file'))
            elif cmd == "3":
                pass
            else:
                break

    def get_date(self, name):
        i = self.I.request('1.File\n2.Input\n')
        if i == 1:
            with open(name, "w") as file:
                result = file.readlines()
        else:
            result = self.I.request('Input:') 
        return result
        

def main():
    Controller(ConsoleReader(), ConsoleWriter()).start()

if __name__ == "__main__":
    main()