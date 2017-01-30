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
            self.O.response("1. Open TextStats module\n2. Open Sorting module\n3. Open UniqHolder module\n4. Test Fibonacci\n5. Exit", 'green')
            cmd = self.I.request("Enter command: ")
            if cmd == "1":
                self.textstats_module(self.get_date('path of text file'))
            elif cmd == "2":
                self.sorting_module(self.get_date('path of numbre file'))
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
    
    def sorting_module(self, date):
        sort = {'1':so.quick_sort, '2':so.merge_sort, '3':so.radix_sort}
        array = list(map(int, date.split()))
        self.O.response('1.quick_sort\n2.merge_sort\n3.radix_sort','red')
        sort_number = self.I.request('Input:') 
        self.O.response(str(sort[sort_number](array)))
        self.O.response('='*50,'blue')

    def textstats_module(self, date):
        for i,j in se.word_analysis(date).items():
            self.O.response('{}--{}'.format(i,j))
        math = se.sentence_analysis(date)
        self.O.response('average - {}\nmedian - {}'.format(math['average'],math['median'])) 
        self.O.response('='*50,'blue')



def main():
    Controller(ConsoleReader(), ConsoleWriter()).start()

if __name__ == "__main__":
    main()