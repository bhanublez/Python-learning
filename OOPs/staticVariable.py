# class Test:
#     x=10
# t=Test()
# print(t.__dict__)
# print(Test.__dict__)
# Test.x=50
# t.x=1000
# print(Test.__dict__)
# print(t.x)
# print(t.__dict__)

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


