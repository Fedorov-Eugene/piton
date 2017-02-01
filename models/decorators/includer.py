from ..controllers.command import Command
from ..views.streams.console.input import Reader
from ..views.streams.console.output import Writer

def use(func):
	return Command(Reader(), Writer(), func)