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
## Local Variable

⚽ Sometimes to meet temporary requirements of programmer,we can declare variables inside a method directly,
such type of variables are called local variable or temporary variables. 

⚽ Local variables will be created at the time of method execution and destroyed once method completes.

⚽ Local variables of a method cannot be accessed from outside of method.

```python
class Test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=2000
        print(a)
        print(b)

```
### Types of Method

    1. Instance Method
        The method we use inside instance variable is known as intance method.
        Inside Instance method decleration i have to pass the self argument.
        By using self variable inside method we can access instance variable.
        To call these method inside we self variable and outside using object reference.

```python
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def s_add(self,add):
        self.add=add
        return(self.add)
    def display(self):
        print("name",self.name)
        print("marks",self.marks)
        print("address of studnet",self.s_add("durga nagar"))
s=Student("bhanu",100)
s.display()
```
    2. class Method
    
Inside method implementation if we are using only class variables (static variables), 
then such type of methods we should declare as class method.

⚽ We can declare class method explicitly by using @classmethod decorator.

⚽ For class method we should provide cls variable at the time of declaration 

⚽ We can call classmethod by using classname or object reference variable.
    
    
```python
#Program to track the Number of Objects created for a Class:
class CheckKaro:
    count=0
    def __init__(self):
        CheckKaro.count+=1
    def diplay(self):
        print(self.count)
ch1 =CheckKaro()
ch1.diplay()
ch2=CheckKaro()
ch2.diplay()
ch3=CheckKaro()
print("Total number of objects:",CheckKaro.count)
```
    
    3. Static Method

⚽ In general these methods are general utility methods.

⚽ Inside these methods we won't use any instance or class variables. 

⚽ Here we won't provide self or cls arguments at the time of declaration.

⚽ We can declare static method explicitly by using @staticmethod decorator 

⚽ We can access static methods by using classname or object reference

```python
class checku:
    p=10
    q=20
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print(self.p+self.q)
    @staticmethod
    def add(x,y):
        print("Accesing class value in staic method",checku.q)
        print("The sum is ",x+y)
    def mul(x,y):
        print("The Mul is ",x*y)

ch=checku(5,6)
ch.add(5,8)
ch.mul(4,1)
```

### Garbage Collection

```python
import gc
print(gc.isenabled())
gc.disabled()
print(gc.isenabled())
```

### destructor

```python
import time
class Test:
    def __init__(self):
        print("Object created")
    def __del__(seld):
        print("Your last wish")
t1=Test()
```

# Phase -II

Using one class member inside another class

```python
# composition
import time
class Engine:
    etype="four stroke"
    def __init__(self):
        self.company="tata"
    def __del__(self):
        print("releasing all engine resources")
    def detail(self):
        print("engine functionality")
class Car:
    def __init__(self):
        self.engine=Engine()
    def __del__(self):
        print("releasing all car resources")
        time.sleep(3)
    def car_detail(self):
        self.engine.detail()
        print(self.engine.etype)
        
c=Car()
c.car_detail()
del c
```

```python
# aggregation
class Car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def __del__(self):
        print("car is releasing resources")
    def car_info(self):
        print(self.name,self.color)
class Emp:
    def __init__(self,name,add,car):
        self.name=name
        self.add=add
        self.car=car
    def __del__(self):
        print("emp release")
    def emp_car_info(self):
        self.car.car_info()
        
c=Car("TUV","black")
emp=Emp("rahul","vidisha",c)
emp.emp_car_info()
del emp
c.car_info()
```



