# Function in Python

1. Function is block od code which is used to perform a specific task.
2. Its is used to break the code into small parts.
3. And increase the reusability of code.
4. Function is defined by using def keyword.
5. Function is called by using function name with parenthesis.
6. Function can be called any number of times.

## Types of Function

1. Built-in Function
2. User-defined Function

## None is also Object Proof

```python
    def hello():
    print("Hello Logo")
    a=hello()
    print("a stor: ",a,"type: ",type(a))
    
    #a stor:  None type:  <class 'NoneType'
```

## Parameter in Function

1. Parameter is used to pass the value to function.
2. Parameter is defined in function definition.
3. Parameter is used to make function more dynamic.

### Multiple object can be passed in function

```python
    def add(a,b):
    print("Addition is: ",a+b)
    add(10,20)
    add(10.5,20.5)
    add("Logo","Bhanu")
```

## Types of Arguments

1. ### Positional Arguments

    1. It is also called as Required Arguments.
    2. It is used to pass the value to function by position.
    3. It is used to pass the value in sequence.

```python
    def wish(name,msg):

    print(f"Hello {name} {msg}")

    wish("Raj","Good Morning")
```

2. ### KeyWord Arguments

    1. It is also called as Named Arguments.
    2. It is used to pass the value to function by name.
    3. It is used to pass the value in any sequence.
    4. It is used to pass the value to specific parameter.

    ```python
    def wish(name,msg):
    print(f"Hello {name} {msg}")
    wish("Raj",msg="Good Morning")
    ```

3. ### Default Arguments

        1. It is used to assign the default value to parameter.
        2. It is used to make parameter optional.
        3. It is used to make function more flexible.
    
```python
    def wish(name,msg="Good Morning"):
    print(f"Hello {name} {msg}")
    wish("Raj")
    wish("Raj","Good Night")
```

## Overloading in Python
    1. It is not supported in Python.
    2. It is used to create multiple function with same name but different parameter.
    3. It is used to make function more flexible.
    4. It is used to make function more dynamic.
    5. There for function overloading is possible in Python.

 ### example
 
```python
    def add(a,b):
    print("Addition is: ",a+b)
    def add(a,b,c):
    print("Addition is: ",a+b+c)
    add(10,20)
    add(10,20,30)
```


## Types of variable in Python

    1. Local variable: Written within scope of function
    2. Global Variable: Which is used outside the scope of function 

    Example:

```python
        a=0 #Global variable
        def fun(a):
        b=0 #local variable
```

### **Assigning value to Global Variable**

```python
a=77 #Global variable
def fun(b):
    d=b+b #local variable
    print(d)
    print(globals()['a'])
fun(10)
```
## Nameless function or Lambda function or Anonymous function
## Syntax: lambda arguments: expression

```python
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

``````

## Special Function
1. ### Map function
    1. It is used to apply function on each element of sequence.
    2. It is used to apply function on each element of list.
    3. It is used to apply function on each element of tuple.
    4. It is used to apply function on each element of set.
    5. It is used to apply function on each element of dictionary.
    6. It is used to apply function on each element of string.
    

```python 
    def add(a):
    return a+10
    l=[10,20,30,40,50]
    l1=list(map(add,l))
    print(l1)
    #Converting directly the list elements into int
    x=list(map(int,input().split()))
    print(x)

```

## Filter Method
```python
#1.Normal Procedure
listt=[1,3,5,1,5,2,54]
evenList=[]
oddList=[]
def even(a):
    return a%2==0
for i in listt:
    if even(i):
        evenList.append(i)
    else:
        oddList.append(i)
print(evenList)
print(oddList)

#2.Filter Method
#filter(function,iterable)
l=[1,3,5,1,5,2,54]
y=lambda x:x%2==0
x=list(filter(y,l))
print(x)

s=lambda *x:list(filter(lambda x:x%2==0,x))
print(s(1,2,3,4,5,6))
```
## Reduce Method

    1. It is used to reduce the sequence into single value.
```python
from functools import reduce
result=reduce(lambda x,y:x+y,range(1,100))

```
## Function Aliasing

    1. It is used to give another name to function.
    2. It is used to make function more flexible.
    3. It is used to make function more dynamic.
    4. It is used to make function more readable.
```python
def hello():
    print("Hello World")
s=hello
s()
print(s())
```

## Abstraction
    1. It is used to hide the implementation details.
    2. It is used to make function more secure.
    3. It create an Illusion
Example: Nested Function concept
```python
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

```

## Decorator Function

    1. It used to enhance the already existing function funtionality
```python
#Advance Decorator function
def decor1(func):
    def inner():
        x=func()
        return x*x
    return (inner)

def decor(fucn):
    def inner():
        x=fucn()
        return 2*x
    return (inner)

@decor1
@decor
def num():
    return (10)
print(num())
```

## Gnerator function

1. It uses `yield` key
Example:-

```python
    dey mygen():
        yield 'A'
        yield 'B'
        yield 'C'
    print(type(mygen))
    g=mygen()
    
        
```
