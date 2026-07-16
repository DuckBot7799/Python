# Data Types =>

#  Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

#  To get the data type, we have to use type() function to get the data type of the variable etc. Example -


# INTEGER
x = 90
print(type(x))
# Result => The data type of x will be int means integer or in simple words, it means number.
# Better Explanation => int means a whole number without a decimal point.


# STRING
y = "Cat"
print(type(y))
# Result => We got str data type which means string or in simple words it means word/text.

# Complex Data Types - If a number contains j, Python calls it a complex number. => Example:


# COMPLEX
x = 5j
print(type(x))
# x's value is 5j means it has a complex value.


# LISTS
#  - Group of variables that can be changed.
# BETTER EXPLANATION => A list is a collection of multiple values that can be changed after creation.
z = ["Apple", "Mango", "Watermelon"]
print(type(z))
# It uses more memory, and it is slower to be read by the system.


# TUPLE
#  - Same as Lists, but the difference is that it cannot be changed once created.
# It uses less memory, also it is faster to be read by the system
M = ("Note", "Mobile", "Pencil")
print(type(M))

# RANGE
# It is used to create a sequence of numbers.
# To create a range. First create a variable. - num_range => Then set range() to 30.
# Then use print(list(*name*)) to unpack the range. Also to get data type, use type() inside print() and inside type(), put the variable name. EXAMPLE:
num_range = range(30)
print(list(num_range))
print(type(num_range))
# The sequence of number starts from 0. Not 1. So 10 isn't included, (0-9)

# DICT
# Python dictionary (dict) is a digital container that stores information in key-value pairs, acting just like a real-world language dictionary. EXAMPLE:

dictionary = dict(
    name="XYZ",
    age=20,
    country="India"
)

print(dictionary)
