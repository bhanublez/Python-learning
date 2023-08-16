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
