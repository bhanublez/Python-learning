#Given a list of numbers, return a list where all adjacent
# equal elements have been reduced to a single element, 
#so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new 
#list or modify the passed in list.

list=eval(input("List data enter karo: "))
print(list)
i=0
while i<len(list)-1:
    if(list[i]==list[i+1]):
        list.pop(i)#removing last element from the list
    else:
        i+=1
print(list)
