#Given three digit number in string format in range of 001 tO 1000, all digits are unique,Number form should be odd
l=[]
for i in range(10):
    for j in range(10):
        for k in range(10):
            if i!=j and j!=k and k!=i:
                s=int(str(i)+str(j)+str(k))
                if(s%2!=0):
                    l.append(str(i)+str(j)+str(k))
print(l)
print(len(l))