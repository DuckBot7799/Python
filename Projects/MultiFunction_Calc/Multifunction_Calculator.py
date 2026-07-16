import operator
import time

# Dictionary mapping symbols to operator functions
OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

print("Opening App...")
time.sleep(2)
print("")
print("Checking System Compatibility...")
time.sleep(2)
print("Checking Version...")
time.sleep(1)
print("----------------------------------------------")
print("System Supported...")
print("----------------------------------------------")
time.sleep(2)
print("Preparing Startup...")
time.sleep(2)

print("")
print("----------------------------------------------")
print("Welcome to the Multi-Purpose Calculator®")
print("----------------------------------------------")
print("")

time.sleep(2)
print("Generating Input Prompt...")
time.sleep(1.5)
print("")

# Step 1: Get the first number
while True:
    try:
        a = float(input("Enter Your First Number          :  Rs.  "))
        break
    except ValueError:
        print("You Have Given Wrong Input, Enter Correctly.")

time.sleep(1)
print("")

# Step 2: Get the mathematical operator
while True:
    op_choice = input("Enter Operator (+, -, *, /)      :       ")
    if op_choice in OPERATORS:
        break
    print("Invalid operator! Please enter +, -, *, or /.")

time.sleep(1)
print("")

# Step 3: Get the second number
while True:
    try:
        b = float(input("Enter Your Second Number         :  Rs.  "))
        # Prevent division by zero error
        if op_choice == "/" and b == 0:
            print("Error: Division by zero is not allowed.")
            continue
        break
    except ValueError:
        print("You Have Given Wrong Input, Enter Correctly.")

time.sleep(2)
print("")
print("Calculating Your Given Numbers...")
time.sleep(2.5)
print("Almost There...")
time.sleep(2)

# Step 4: Perform the dynamic calculation
calc_function = OPERATORS[op_choice]
result = calc_function(a, b)

print("")
print("------------------------------------------------------------")
print(f"The Result Of Your Calculation Is:   {result} (INR)")
print("------------------------------------------------------------")

print("")
time.sleep(1.5)
print("Activating AUTO EXIT...")
time.sleep(1.5)
print("Exiting...")
time.sleep(1.5)
print("Thanks For Using Calculator®! 😁")
