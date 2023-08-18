def outer():
    def inner1():
        print("Hello function 1")
    def inner2():
        print("hello function 2")
    return (inner1,inner2)
s=outer()
for i in s:
    i()
s=outer()[-1]()


