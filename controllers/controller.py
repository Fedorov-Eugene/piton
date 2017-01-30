from .command import Command
class Controller(object):
    """Controller"""
    def __init__(self, input_, output):
        super(Controller, self).__init__()
        self.I = input_
        self.O = output
        self.cmd = {"help": Command(self.wait, self.O.response ,self.introduce) }

    def wait(self, *whatever):
        pass

    def add(self, name, func):
        self.cmd[name.lower()] = func
        return self

    def introduce(self, *whatever):
        self.O.response("Command list: ")
        for counter, key in enumerate(self.cmd):
            self.O.response(str(counter) + ". " + key.capitalize())

    def no_command_error(self, name):
        self.O.response("There is no command with name '" + str(name) + "', please try again.")

    def retrieve_command(self, name):
        return self.cmd[name] if name in self.cmd else Command(name, self.O.response, self.no_command_error)

    def start(self, arg = None):
        if not arg:
            self.introduce()
            prompt = self.I.request("Enter: ").lower()
        else:
            prompt = arg    
        while self.retrieve_command(prompt):
            self.retrieve_command(prompt)();
            prompt = self.I.request("Enter: ").lower()
        
    def generate_command(self, func, prom = ""):
        return Command(self.I.request, self.O.response, func, prom)
            
    def silent_command(self, func):
        return Command(None, self.O.response, func)

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


