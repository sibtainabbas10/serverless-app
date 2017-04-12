from __future__ import print_function
from index import my_func

def lambda_handler(event, context):
	print("Hello start")
	my_func()
	print("Hello end")