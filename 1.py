from unittest import result
from log_writer import log_writer



@log_writer
def calculator(a, b):
	return a + b


print(calculator(a=7, b=5))
