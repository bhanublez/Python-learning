list1="a4b3c2"
list2="aaaabbbcc"
i=0
j=0
result=""
n1=len(list1)
n2=len(list2)
while n1>0 or n2>0:
    if n1>0:
        result+=list1[i]
        i+=1
        n1-=1
    if n2>0:
        result+=list2[j]
        j+=1
        n2-=1
print(result)