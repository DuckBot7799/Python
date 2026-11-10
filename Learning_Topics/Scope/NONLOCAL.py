def mylocal1():
	x = "Jane"

	def mylocal2():
		nonlocal x
		x = "HELLO"

	mylocal2()
	return x


print(mylocal1())

#The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.
