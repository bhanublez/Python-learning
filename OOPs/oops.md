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
    c. Outside instance methods