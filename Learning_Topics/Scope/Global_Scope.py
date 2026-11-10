#Global Scope
#A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#Global variables are available from within any scope, global and local.


#A variable created outside of a function is global and can be used by anyone:

a = 500


def myglobal():
	print(a)
	return


myglobal()
