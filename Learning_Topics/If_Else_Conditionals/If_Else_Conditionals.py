# If-Else & Elif basic conditional statement.

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