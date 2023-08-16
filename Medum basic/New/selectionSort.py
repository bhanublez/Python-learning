#Selection sort
list=eval(input("Enter the data:"))
print(list)

#Selection sort login
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if(list[i]>list[j]):
            list[i],list[j]=list[j],list[i]#swapping
print(list)
#q1=time.clock()