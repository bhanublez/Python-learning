#Given three digit number as input, we need to find out no. of possible digit in that range in all digit odd
#all the digit must be different
l=[]
for i in range(100,999+1):
    n=i
    flag=False
    while(n>0):
        r= n%10
        check=[]
        check.append(r)
        if(r%2==0):
            flag=True
        n=n//10
    if(flag==False):
        l.append(i)
print(l)
print(len(l))