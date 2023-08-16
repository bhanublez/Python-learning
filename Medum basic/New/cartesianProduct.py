#Write a program to find out the Cartesian product 
# of two set and also verify that number of elements 
# in product set is equal to the number of element in 
# set1 multiplied by number of element in set two
set1=eval(input("enter set 1 value "))
set2=eval(input("enter set 2 value"))
set3=set()
print(type(set3))
for i in set1:
    for j in set2:
        set3.add((i,j))
print(set3)
 