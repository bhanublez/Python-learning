class P:
    def __init__(self) -> None:
        print("P")
        print(id(self))
        self.b=10#By default there in not any private funtion and variable
class C(P):
    # pass
    def __init__(self) -> None:
        super().__init__()
        print("c")
c=C()
print(id(c))
# print(c.b)

# class B:
#     def __init__(self) -> None:
#         super().__init__()
#         print("Construnctor called")

# b=B()
