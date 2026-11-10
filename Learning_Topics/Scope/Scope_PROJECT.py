# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

from time import sleep


# NUMBER SUM PROGRAM USING FUNCTION
def my_scope():
	z = int(input("Give Number: "))
	sleep(1)
	x = int(input("Give Number: "))
	sleep(1)
	a = z
	b = x
	print("")
	sleep(2)
	print("Processing...")
	sleep(1.5)
	print("It may take a while to add, because this system relies on legacy threading...")
	sleep(1.5)
	print("Here it goes!..")
	sleep(1)
	print("")
	print("ANSWER 👇")
	c = (a + b)
	return print(c)


# FUNCTION CALLED
print("==============================================================")
sleep(1)
print("WELCOME TO NUM-SUM PROGRAM! 😁")
sleep(1)
print("-----------------------------------------------------------------------------------")
print("Loading interactive page...")
print("")
my_scope()
print("")
sleep(2)
print("Thanks for using our program!")
sleep(1)
print("----------------------------------------------------------------------------------")
print("==============================================================")
