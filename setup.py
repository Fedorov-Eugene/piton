import mathstats.search as se
import mathstats.sort as so
import mathstats.fib as fi
import mathstats.uniqholder as uh
from views.console_input import ConsoleReader
from views.console_view import ConsoleWriter
import controllers.controller
from . import settings

def sorting_controller(cin, cout):
	tmp = Controller(cin, cout)
	tmp.add("quick sort", tmp.O.response(so.quick_sort(map(int, tmp.I.request("Enter numbers vis spacebars: ").split(" ")))))
	tmp.add("merge sort", tmp.O.response(so.merge_sort(map(int, tmp.I.request("Enter numbers vis spacebars: ").split(" ")))))
	tmp.add("radix sort", tmp.O.response(so.radix_sort(map(int, tmp.I.request("Enter numbers vis spacebars: ").split(" ")))))
	tmp.add("back", False)
	return tmp

def fib_controller(cin, cout):
	tmp = Controller(cin, cout)
	tmp.add("generate", tmp.O.response(fi.fibonacci(int(tmp.I.request("Enter number: ")))))
	tmp.add("back", False)
	return tmp

def search_controller(cin, cout):
	tmp = Controller(cin, cout)
	tmp.add("email check", tmp.O.response(se.isemail(tmp.I.request("Enter email: "))))
	tmp.add("float number check", tmp.O.response(se.isfloat(tmp.I.request("Enter number: "))))
	tmp.add("url parse", tmp.O.response(se.urlparse(tmp.I.request("Enter url: "))))
	tmp.add("sentense analysis", tmp.O.response(se.sentence_analysis(mp.I.request("Enter sentence: "))))
	tmp.add("back", False)
	return tmp

def uniq_controller(cin, cout):
	tmp = Controller(cin, cout)
	self.uhs = self.uhs or UniqHolder()
	self.uhs.load(DEFAULTS["uniq_load_path"])
	tmp.add("add item", uh.add(tmp.I.request("Enter item or items: ").split(" ")))
	tmp.add("find item", tmp.O.response(uh.find(tmp.I.request("Enter item ot items: ").split(" "))))
	tmp.add("remove item", uh.remove(tmp.I.request("Enter item: ")))
	tmp.add("list items", tmp.O.response(uh.list()))
	tmp.add("back", False)
	return tmp

def main():
	cin = ConsoleReader()
	cout = ConsoleWriter()
    SORT_CNTR = sorting_controller(cin, cout)
    FIB_CNTR = fib_controller(cin, cout)
    SRCH_CNTR = search_controller(cin, cout)
    UNQ_CNTR = uniq_controller(cin, cout)
    APP_CNTR =  Controller(cin, cout).add("sorting", SORT_CNTR.start()).add("fibonacci", FIB_CNTR.start()).add("search", SRCH_CNTR.start()).add("unique holder", UNQ_CNTR.start())
    APP_CNTR.start()
    
if __name__ == "__main__":
    main()