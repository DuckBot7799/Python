# Variables are containers for storing data values.
# A variable is created the moment you first assign a value to it.

a = 10
b = 50
print(a)
print(b)
print(a + b)

# We can change the variable type by putting str, float, int and then () on the right then value inside like 90
c = str(90)
print(c)


# To get the variable type, we can use type() inside print()

print(type(c))
# Result will be str means string


# Python allows you to assign values to multiple variables in one line

x, y, z = "Apple", "Banana", "Carrot"
print(x, y, z)

# Each variable gets a different value, not the same value. So it goes like respectively, x = apple, y = banana, z = carrot


# One value to multiple variables:

a = b = c = "Apple"
print(a, b, c)

# Result => This will put the value to all given variables/it will make the value same to all given variables
