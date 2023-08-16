#eval function is used to convert the string to list
# list=eval(input("Enter the data : "))
# print(list)
# print(type(list))
#creating a list with list function
# list1=list((input("Enter the data : ").split(",")))
# print(list1)

#len function
# print(len(list1))

#count function
# print(list1.count("1"))

#append function
#insert data at the end of the list
# list1.append("86")
# print(list1)

#insert function
#insert data at the specifeid index
# list1.insert(2,"420")

list=[1,2,3,4,5,6,7,8,9]
list2=["Ajajaj","Bababab","Cacacac"]

#extend function
#insert data at the end of the list
# list=list+list2
# print(list)
# list.extend([10,"bhanu","patap","Singh"])
# print(list)

#pop function
#remove the last element from the list
# print(list)
# print(list.pop())
# print(list)

#remove function
#remove the specified element from the list
# print(list)
# list.remove(5)
# print(list)

#ordering of list data

#reverse function used to reverse the data of list
# print(list.reverse())#work on inplace concept
# print(list)

#sort function used to sort the data of list
# print(list.sort())#work on inplace concept/
# print(list)
# str=['bhanu','patap','singh']#Integer add error return
# print(str.sort())
# print(str)

#Use sort function to sort in decending order
# list.sort(reverse=True)
# print(list)

#Aliasing and cloning of list
#Aliasing is the process of giving another name to the list
# x=[1,2,3,4,5]
# y=x#referencing took place here
# print(id(x),id(y))
# y=x[:]#form new object
# print(y)
# print(id(x),id(y))
# y=x.copy()#form new object
# print(y)
# print(id(x),id(y))
# y=x*3#form new object
# print(y)

#clear function
#clear the data of list
# print(list)
# list.clear()
# print(list)

# n=int(input("Enter the number of elements : "))
# newlist=[int(i**2) for i in range(n)]
# print(newlist)

#list comprehension is used create list in one line of code 
# newlist=list(range(n))
# print(newlist)
nn=[int(i**2) for i in range(1,11) if i%2==0]

# nn=[int(i**2) for i in input("enter the data ").split(" ") ]
print(nn)
