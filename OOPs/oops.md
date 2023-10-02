# Introduction to Object oriented programming

1. Class is blue Print og object
2. Class is having attributes and bevaour
3. properties--.data,behaviour is method
4. properties--> Varaible
5. actions-->methods

    ```python
    class Student:
        """this is student string"""
    
    class Teacher:
        """this is teacher string"""
    ```

## What is Object?

1. Object is a instance of class
2. physical existence of class is nothing but its a object

```python
s=Student()
print(type(s))
# s is refrence variable pointing to sudent type of object
class Student:
    """This is a Student class"""
    # How to defince constructor in class
    def __init__(self,roll,name,marks): #return error i self is absent
        self.roll=roll
        self.name=name
        self.marks=marks
    def s_info(self):
        print("My name is ",self.name)
s=Student(1,"bhanu",99.99)
s.s_info()

```
## Self Concept
1.self is mandatory argument for constructor and instance methods
2. Here self is not any keyword, we can use any name at place of self like this,bhanu,anything etc
3. By using self/-- using we can excess the instance variable and instance method of object
4. self/-- is default variable which is pointingg to the current object

 ```python
 class Test:
    def __init__(self):
        print("Constructor executed")
t1=Test()
t2=Test()
 ```
## Types of variable in pythghon
1. Instance varibale: (Object level)
Here value of varaible vary from variable to variable.
For Every object a seprate copy of instance variable is created.
    a. Inside constructor using self 
    b. Inside instance method using self
    c. Outside instance methods (By using object refference)

```python
class Test:
    def __init__(self):
        #inside constructor
        self.a=10
    def m(self):
        #insie instance method
        self.b=20

t=Test()
print(t)
#We have special magic variable
print(t.__dict__)

t.m()
print(t.__dict__)

#i am declaring the varaible outside the class
t.c=20
print(t.__dict__)

t1=Test()
t1.m()
print(t1.__dict__)

#In the pythen store the refence of the objext in dictonary in meta data
```
## How to access instance varaible

1. Outside class using reference variable
2. inside class using self

## Staic Variable
1. Declaration os static method
    1. Inside class but outside all method
    2. Inside constructor by using classname
    3. inside instance method using classname
    4. inside static method using classname
    5 inside class method using class name
```python
class Test:
    x=10
t=Test()
print(t.__dict__)
print(Test.__dict__)
Test.x=50
t.x=1000
print(Test.__dict__)
print(t.x)
print(t.__dict__)
````

2. How to access staic variable

    a. Inside constructor: by using either self or classname
    b. Inside instance method: by using either self or classname
    c. inside class method: by using either class variable or classname
    d. inside static method: by using class name
    e. from outside of class: by using either object reference or classname
`

```python 
print("Accessing static method")
class Test:
    x=10
    #inside constructor
    def __init__(self):
        print(self.x)#Accesing using self 
        print(Test.x)#using class name

    #inside instance method
    def check(self):
        print(self.x)#Accesing using self 
        print(Test.x)#using class name

t=Test()
t.check()
```

## Data Types

```python
int
float
bool
str
list
tuple
set
dict
```
