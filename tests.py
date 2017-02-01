import sys
import models.sort as module
import datetime
import random
from views.console_input import request
from views.console_view import response

def suppose(get, awaits):
	if get == awaits:
		response("="*80 + "\nTest passed\n" + "="*80, 'green')
	else:
		response("="*80 + "\nTest failed\n" + "="*80 + "\nYour result: " + str(get) + "\nExpected: " + str(awaits), 'red')

def speedcheck(func, iter, *test_data):
	start = datetime.datetime.now()
	for i in range(iter):
		func(test_data)
	finish = datetime.datetime.now()
	response(str(finish-start) + " time elapsed")

