import time

time.sleep(0.5)
print("Opening Addition Calculator®...")
time.sleep(2)

print("")
print("----------------------------------------------")
print("Welcome to the Addition Calculator®")
print("----------------------------------------------")
print("")

time.sleep(2)
print("Generating Input Prompt...")
time.sleep(2)
print("")

while True:
    try:
        a = float(input("Enter Your First Number          :  Rs.  "))
        break

    except ValueError:
        print("You Have Given Wrong Input, Enter Correctly.")

time.sleep(1)
print("")
# ---------------------------------------------------------------------------------------
while True:
    try:
        b = float(input("Enter Your Second Number       :  Rs.  "))
        break

    except ValueError:
        print("You Have Given Wrong Input, Enter Correctly.")

time.sleep(2)
print("")
print("Calculating Your Given Numbers...")
time.sleep(3)
print("Almost There...")
time.sleep(2)

print("")
print("------------------------------------------------------------")
print(f"The Sum Of Your Given Number Is  :   {a + b} (INR)")
print("------------------------------------------------------------")

print("")
time.sleep(2)
print("Activating AUTO EXIT...")
time.sleep(2)
print("Exiting...")
time.sleep(1)
print("Thanks For Using Addition Calculator®! 😁")
