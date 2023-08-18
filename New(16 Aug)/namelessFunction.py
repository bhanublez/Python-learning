## Nameless function or Lambda function or Anonymous function
## Syntax: lambda arguments: expression
x=lambda a:a+10
print(x(5))

#Using normal function
def add(x,y):
    return x+y
print(type(add))
print(add(5,6))

#Using lambda function as an argument
m=lambda x,y:x+y
print(type(m))
print(m(5,6))

#Check functioning
import dis
#for normal function
dis.dis(add)
#for Lambda function
dis.dis(m)

#Greater value print
m=lambda x,y,z:x if x>y and x>z else y if y>z else z
print(m(5,6,7))



