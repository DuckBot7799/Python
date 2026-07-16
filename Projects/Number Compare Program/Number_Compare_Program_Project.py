import time

time.sleep(5)
print("Starting The Program...")
time.sleep(1.5)
print("Loading User Interface...")
time.sleep(2)
print("")
# =======================================================================================================
print("====================================================")
time.sleep(0.5)
print("====================================================")
time.sleep(0.5)
print("Welcome To Number Compare Program")
time.sleep(0.5)
print("====================================================")
time.sleep(0.5)
print("====================================================")
print("")
time.sleep(1.5)
print("Generating User Input Prompt...")
print("")
time.sleep(0.5)
# =======================================================================================================
print("")
a = input("Enter Your First Number       :   ")
time.sleep(0.5)
print("==========================")
print("Loading Second Input Prompt...")
print("==========================")
time.sleep(0.5)
b = input("Enter Your Second Number  :   ")
time.sleep(1.5)

# =======================================================================================================
print("")
print("Comparing Values...")
time.sleep(1.5)

# =======================================================================================================
time.sleep(1)
print("Almost There...")
print("")
time.sleep(1)

# ==========================================================
print("=====================================================")
time.sleep(1)
if a < b:
    print("Your Second Number is Greater Than First Value.")
time.sleep(1)
if a > b:
    print("Your First Number is Greater Than Second Value.")
time.sleep(1)
if a == b:
    print("Your Given Values Are Same!")
print("=====================================================")
# ==========================================================

time.sleep(2)
print("----------------------------------------------------------------------")
time.sleep(1)
if (bool(a) == bool(b)):
    print(f"Final Result (T/F) : First Number is {bool(a)} & Second Number is also {bool(b)} In BOOLEAN Type")

elif(bool(a) != bool(b)):
    print(f"Final Result (T/F) : First Number is {bool(a)} & Second Number is {bool(b)} In BOOLEAN Type")

# print(f"Final Result (T/F) : First Number is {bool(a)} & Second Number is {bool(b)} In BOOLEAN Type")
time.sleep(1)
print("----------------------------------------------------------------------")
print("")
time.sleep(1)
print("Exiting...")
time.sleep(1)