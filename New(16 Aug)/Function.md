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

    def hello():
    print("Hello Logo")
    a=hello()
    print("a stor: ",a,"type: ",type(a))

*a stor:  None type:  <class 'NoneType'*

## Parameter in Function

1. Parameter is used to pass the value to function.
2. Parameter is defined in function definition.
3. Parameter is used to make function more dynamic.

### Multiple object can be passed in function

    def add(a,b):
    print("Addition is: ",a+b)
    add(10,20)
    add(10.5,20.5)
    add("Logo","Bhanu")

###