class object:
    def __init__(self) -> None:
        print("Object object")
class A(object):
    def __init__(self) -> None:
        super().__init__()
        print("Object A")

class B(object):
    def __init__(self) -> None:
        super().__init__()
        print("Object B")

class C(object):
    def __init__(self) -> None:
        super().__init__()
        print("Object C")


class X(A,B):
    def __init__(self) -> None:
        super().__init__()
        print("Object X")

class Y(B,C):
    def __init__(self) -> None:
        super().__init__()
        print("Object Y")


class P(X,Y,C):
    def __init__(self) -> None:
        super().__init__()
        print("Object P")

# a=A()
# b=B()
# c=C()
# x=X()
# y=Y()
p=P()
