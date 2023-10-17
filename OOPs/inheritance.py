class p:
    a=10
    def __init__(self):
        self.b=20
    @classmethod
    def m1(self):
        print('parent instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')
class C(p):
    pass
c=C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()
