
# #Filter Method
# ##Normal Procedure
# listt=[1,3,5,1,5,2,54]
# evenList=[]
# oddList=[]
# def even(a):
#     return a%2==0
# for i in listt:
#     if even(i):
#         evenList.append(i)
#     else:
#         oddList.append(i)
# print(evenList)
# print(oddList)

# ##Filter Method
# #filter(function,iterable)
# l=[1,3,5,1,5,2,54]
# y=lambda x:x%2==0
# x=list(filter(y,l))
# print(x)

# s=lambda *x:list(filter(lambda x:x%2==0,x))
# print(s(1,2,3,4,5,6))


# #Map method
# def add(a):
#     return a+10
# l=[10,20,30,40,50]
# l1=list(map(add,l))
# print(l1)

# #Converting directly the list elements into int
# x=list(map(int,input().split()))
# print(x)

# #Converting directly into the provided datatype
# x=list(map(eval,input().split()))
# print(x)

#WAP to program to filter out the even length string f
# rom given typle of string in lambda function
x=("bhanu","anmol","ravi","raju","panku")
y=lambda x:len(x)%2==0
print(list(filter(y,x)))