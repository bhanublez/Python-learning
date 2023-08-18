#Variable Argument
def fun(*n):
    print(n)

#type of variable
a=77 #Global variable
def fun(b):
    d=b+b #local variable
    print(d)
    print(globals()['a'])

fun(10)