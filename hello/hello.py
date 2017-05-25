from __future__ import print_function
from .util.index import *

def lambda_handler(event, context):
	print("Hello start")
	print(my_func())
	print("Hello end")