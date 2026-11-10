def mylocal1():
	x = 10

	def mylocal2():
		nonlocal x
		x = 90

	mylocal2()
	return x


print(mylocal1())

#The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.
