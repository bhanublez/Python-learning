# # # # # # # # # # # # # #Ram decided to write a function divide (a,b) where a
# # # # # # # # # # # # # # and b are integer argument this function this function give 
# # # # # # # # # # # # # # the result of division of a by b but when he run
# # # # # # # # # # # # # #Use decorative function to handle the exception in the divide function
# # # # # # # # # # # # # #don't use try function


# # # # # # # # # # # # # def decor(func):
# # # # # # # # # # # # #     def inner(a,b):
# # # # # # # # # # # # #         if b==0:
# # # # # # # # # # # # #             print("Zero not allowed")
# # # # # # # # # # # # #         else:
# # # # # # # # # # # # #             return func(a,b)
# # # # # # # # # # # # #     return inner

# # # # # # # # # # # # # @decor
# # # # # # # # # # # # # def num(a,b):
# # # # # # # # # # # # #     return a/b
# # # # # # # # # # # # # print(num(10,6))
# # # # # # # # # # # # nums = set([1,1,2,3,3,3,4,4])

# # # # # # # # # # # # print(len(nums))
# # # # # # # # # # # x=12

# # # # # # # # # # # def f1(a,b=x):

# # # # # # # # # # #     print(a,b)

# # # # # # # # # # # x=15

# # # # # # # # # # # f1(4)
# # # # # # # # # # def san(x):

# # # # # # # # # #     print(x+1)

# # # # # # # # # # x=-2

# # # # # # # # # # x=4

# # # # # # # # # # san(12)
# # # # # # # # # t = (1, 2, 4, 3, 8, 9)

# # # # # # # # # [t[i] for i in range(0, len(t), 2)]
# # # # # # # # def foo():

# # # # # # # #     return total + 1

# # # # # # # # total = 0

# # # # # # # # print(foo())
# # # # # # # def foo(fname, val):

# # # # # # #     print(fname(val))

# # # # # # # foo(max, [1, 2, 3])

# # # # # # # foo(min, [1, 2, 3])
# # # # # # def foo(k):

# # # # # #     k[0] = 1

# # # # # # q = [0]

# # # # # # foo(q)

# # # # # # print(q)
# # # # # x = 50

# # # # # def func(x):

# # # # #     print('x is', x)

# # # # #     x = 2

# # # # #     print('Changed local x to', x)

# # # # # func(x)

# # # # # print('x is now', x)
# # # # a={1:5,2:3,3:4}

# # # # print(a.pop(4,9))
# # # a={1:5,2:3,3:4}

# # # a.pop(3)

# # # print(a)
# # d = {"john":40, "peter":45}

# # print(list(d.keys()))
# d = {"john":40, "peter":45}

# d["john"]
a={5,6,7,8}

b={7,8,9,10}

len(a+b)