# A function is a block of code which only runs when it is called.
# A function can return data as a result.
# A function helps to avoid code repetition.
from time import sleep


def my_function():
	sleep(1)
	print("This is a function.")
	sleep(1)
	print("This function is called by writing the name of the function out of the code block.")
	sleep(1)


my_function()
