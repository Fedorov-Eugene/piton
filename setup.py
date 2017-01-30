import argparse
import mathstats.search as se
import mathstats.sort as so
import mathstats.fib as fi
from mathstats.uniqholder import UniqueHolder
from views.console_input import ConsoleReader
from views.console_view import ConsoleWriter
from controllers.controller import Controller
from controllers.command import Command
from settings import DEFAULTS


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('modul', nargs = '?')
    namespace = parser.parse_args()
    return(namespace.modul)

def sorting_controller(cin, cout):
    tmp = Controller(cin, cout)
    tmp.add("quick sort", tmp.generate_command(so.quick_sort_test))
    tmp.add("merge sort", tmp.generate_command(so.merge_sort_test))
    tmp.add("radix sort", tmp.generate_command(so.radix_sort_test))
    tmp.add("back", False)
    return tmp

def fib_controller(cin, cout):
    tmp = Controller(cin, cout)
    tmp.add("generate", tmp.generate_command(fi.fib_array))
    tmp.add("back", False)
    return tmp

def search_controller(cin, cout):
    tmp = Controller(cin, cout)
    tmp.add("email check", tmp.generate_command(se.isemail))
    tmp.add("float number check", tmp.generate_command(se.isfloat))
    tmp.add("url parse", tmp.generate_command(se.urlparse))
    tmp.add("sentense analysis", tmp.generate_command(se.sentence_analysis))
    tmp.add("back", False)
    return tmp

def uniq_controller(cin, cout):
    tmp = Controller(cin, cout)
    holder = UniqueHolder()
    tmp.add("add item", tmp.generate_command(holder.add))
    tmp.add("find item", tmp.generate_command(holder.find))
    tmp.add("remove item", tmp.generate_command(holder.remove))
    tmp.add("list items", tmp.silent_command(holder.list))
    tmp.add("back", False)
    return tmp


def main():
    cin = ConsoleReader()
    cout = ConsoleWriter()
    SORT_CNTR = sorting_controller(cin, cout)
    FIB_CNTR = fib_controller(cin, cout)
    SRCH_CNTR = search_controller(cin, cout)
    UNQ_CNTR = uniq_controller(cin, cout)
    
    

    APP_CNTR = Controller(cin, cout)
    APP_CNTR.add("sorting", SORT_CNTR.silent_command(SORT_CNTR.start))
    APP_CNTR.add("fibonacci", FIB_CNTR.silent_command(FIB_CNTR.start))
    APP_CNTR.add("search", SRCH_CNTR.silent_command(SRCH_CNTR.start))
    APP_CNTR.add("unique holder", UNQ_CNTR.silent_command(UNQ_CNTR.start))
    APP_CNTR.add("exit", False)

    APP_CNTR.start(arguments())

if __name__ == "__main__":
    main()