## Reduce Function
#function tool
# from functools import reduce
# result=reduce(lambda x,y:x+y,range(1,100))

# Function Aliasing 
# Using it/ is possible to assign a different name to a function. This is known as aliasing a function.
def hello():
    print("Hello World")
s=hello
s()
print(s())
