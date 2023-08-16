#Given two lists sorted in increasing order, 
#create and return a merged list of
#all the elements in sorted order
list1=eval(input("Enter the list 1 data:"))
print("List 1 is: ",list1)
list2=eval(input("Enter the list two data:"))
print("List 2 is:",list2)
list3=[] #data merege 
while len(list1)>0 and len(list2)>0:
    if(list1[0]<list2[0]):
        list3.append(list1.pop(0))
    else:
        list3.append(list2.pop(0))
    if(len(list1)==0):
        list3.extend(list2)#Directly join remaing bro
    if(len(list2)==0):
        list3.extend(list1)#Directly join remaing bro
print(list3)