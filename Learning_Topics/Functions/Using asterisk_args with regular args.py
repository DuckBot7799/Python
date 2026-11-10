# Using *args with Regular Arguments
# You can combine regular parameters with *args.
# Regular parameters must come before *args:

def my_function(greeting, *names):
	for name in names:
		print(greeting, name)


my_function("Hello", "Emil", "Tobias", "Linus")


# greeting receives "Hello".
# *names collects the remaining arguments into a tuple

def my_function(*numbers):
	total = 0
	for num in numbers:
		total += num
	return total


print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))
