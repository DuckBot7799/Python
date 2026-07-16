# # In programming you often need to know if an expression is True or False.
# #
# # You can evaluate any expression in Python, and get one of two answers, True or False.
# #
# # When you compare two values, the expression is evaluated and Python returns the Boolean answer
#
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# =========================================================

# a = float(input("Enter your first number here     : "))
# b = float(input("Enter your second number here : "))
#
# if a < b:
#     print("Second number is bigger than first number")
#
# if a == b:
#     print("Both numbers are equal")
#
# if a > b:
#     print("First number is bigger than second number")

# =========================================================

# print(bool("Hello"))
# print(bool(0))

# =========================================================
# c = input("Enter First Value       :   ")
# d = input("Enter Second Value  :   ")
#
# print(bool(c))
# print(bool(d))

# =========================================================

# class myclass():
#     def __len__(self):
#         return 0
#
#
# print(bool(myobj))

# =========================================================

# Use of If & Else:

# def myFunction():
#     return 0
#
#
# if myFunction():
#     print("Yes")
# else:
#     print("No")


# =========================================================

# Use of If & Else:

# def myFunction():
#     a = 5
#     b = 5
#     return a - b
#
#
# if myFunction():
#     print("Yes")
# else:
#     print("No")


# =========================================================

# Use of If & Else:

def myFunction():
    a = float(input("Enter first number     : "))
    b = float(input("Enter second number : "))
    return a - b


if myFunction():
    print("Value Found")
else:
    print("No Value Found")

# =========================================================
# To check whether that object is of a certain data type, so we use
# isinstance

# x = "abc"
# print(isinstance(x, str))

# =========================================================

