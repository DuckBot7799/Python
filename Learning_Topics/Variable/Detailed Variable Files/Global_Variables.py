# Global Variables means variables outside function. Example:
a = 50
print(a)


# To create a function, we have to define it and name it.

def tea():
    print("This is a tea function")

tea()
# We have defined and created a function named tea. Also we have added print function.
# We used tea() to call it.
# Result => "This is a tea function"

# To make variable to be used outside function, we have to use global keyword to convert a local into global.

def firstfunc():
    global x
    x = "abcd"


firstfunc()
print(x)
