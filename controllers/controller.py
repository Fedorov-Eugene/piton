from .command import Command
class Controller(object):
    """Controller"""
    def __init__(self, input_, output):
        super(Controller, self).__init__()
        self.I = input_
        self.O = output
        self.cmd = {"help": Command(self.wait, self.O.response ,self.introduce) }

    def wait(self):
        pass

    def add(self, name, func):
        self.cmd[name.lower()] = func
        return self

    def introduce(self):
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

