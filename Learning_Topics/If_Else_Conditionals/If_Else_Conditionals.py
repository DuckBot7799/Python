# If-Else & Elif basic conditional statement.

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
#
# The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

import time

time.sleep(1)
print("Loading...")

time.sleep(2)
a = input("Enter Your First Number:       ")
time.sleep(1)
b = input("Enter Your Second Number:    ")
time.sleep(1)
print("")
print("Comparing Your Given Values...")
time.sleep(2)

if a > b:
    print(f"Your First Number Is Greater! {a}")

elif a < b:
    print(f"Your Second Number Is Greater! {b}")

elif a == b:
    print(f"Your Both Given Numbers are equal! {a} and {b}")