import sys
import mathstats.sort as module
import datetime
import random

def wrapper(text, symbol):
	print(symbol + text + symbol + '\033[0m')


func = {"quick_sort": module.quick_sort, "merge_sort": module.merge_sort, "radix_sort": module.radix_sort}
option = input("Enter function name to test: ")
print("Let's roll through some Pre-Tests:")

print("\nShould work for empty array")
arr = []
if func[option](arr) == sorted(arr):
	wrapper("="*80 + "\nPre-test passed\n" + "="*80, '\033[92m')
else:
	wrapper("="*80 + "\nPre-test failed\n" + "="*80 + "\nYour result: " + str(func[option](arr)) + "\nExpected: " + str(sorted(arr)), '\033[91m')

print("\nShould work for array from one element")
arr = [1]
if func[option](arr) == sorted(arr):
	wrapper("="*80 + "\nPre-test passed\n" + "="*80, '\033[92m')
else:
	wrapper("="*80 + "\nPre-test failed\n" + "="*80 + "\nYour result: " + str(func[option](arr)) + "\nExpected: " + str(sorted(arr)), '\033[91m')

print("\nShould work for array from negative values")
arr = [-1, -5, -6, -8, -10, 0]
if func[option](arr) == sorted(arr):
	wrapper("="*80 + "\nPre-test passed\n" + "="*80, '\033[92m')
else:
	wrapper("="*80 + "\nPre-test failed\n" + "="*80 + "\nYour result: " + str(func[option](arr)) + "\nExpected: " + str(sorted(arr)), '\033[91m')


print("\nShould work for simple arrays")
arr = [4, 5, 6, 78, 87, 23, 14, 67, 45, 22, 23, 90, 1, 3, 9, 56, 55, 50, 30, 11]
if func[option](arr) == sorted(arr):
	wrapper("="*80 + "\nFirst test passed\n" + "="*80, '\033[92m')
else:
	wrapper("="*80 + "\nFirst test failed\n" + "="*80 + "\nYour result: " + str(func[option](arr)) + "\nExpected: " + str(sorted(arr)), '\033[91m')
print("Time taken for 10000 iterations:")
start = datetime.datetime.now()
for i in range(10000):
	func[option](arr)
finish = datetime.datetime.now()
print(str(finish-start) + " seconds\n")

print("Should work for duplicated numbers")
arr = [10] * 20
if func[option](arr) == sorted(arr):
	wrapper("="*80 + "\nSecond test passed\n" + "="*80, '\033[92m')
else:
	wrapper("="*80 + "\nSecond test failed\n" + "="*80 + "\nYour result: " + str(func[option](arr)) + "\nExpected: " + str(sorted(arr)), '\033[91m')
print("Time taken for 10000 iterations:")
start = datetime.datetime.now()
for i in range(10000):
	func[option](arr)
finish = datetime.datetime.now()
print(str(finish-start) + " seconds\n")

print("Should work for presorted arrays")
arr = list(range(20))
if func[option](arr) == sorted(arr):
	wrapper("="*80 + "\nThird test passed\n" + "="*80, '\033[92m')
else:
	wrapper("="*80 + "\nThird test failed\n" + "="*80 + "\nYour result: " + str(func[option](arr)) + "\nExpected: " + str(sorted(arr)), '\033[91m')
print("Time taken for 10000 iterations:")
start = datetime.datetime.now()
for i in range(10000):
	func[option](arr)
finish = datetime.datetime.now()
print(str(finish-start) + " seconds\n")

print("Should work for reversed arrays")
arr = list(reversed(range(20)))
if func[option](arr) == sorted(arr):
	wrapper("="*80 + "\nFourth test passed\n" + "="*80, '\033[92m')
else:
	wrapper("="*80 + "\nFourth test failed\n" + "="*80 + "\nYour result: " + str(func[option](arr)) + "\nExpected: " + str(sorted(arr)), '\033[91m')
print("Time taken for 10000 iterations:")
start = datetime.datetime.now()
for i in range(10000):
	func[option](arr)
finish = datetime.datetime.now()
print(str(finish-start) + " seconds\n")

print("Should work for REALLY long arrays")
arr = random.sample(range(1000000), 1000000)
if func[option](arr) == sorted(arr):
	wrapper("="*80 + "\nFivth test passed\n" + "="*80, '\033[92m')
else:
	wrapper("="*80 + "\nFivth test failed\n" + "="*80 + "\nYour result: " + str(func[option](arr)) + "\nExpected: " + str(sorted(arr)), '\033[91m')
print("Time taken for 1 iterations:")
start = datetime.datetime.now()
for i in range(1):
	func[option](arr)
finish = datetime.datetime.now()
print(str(finish-start) + " seconds\n")