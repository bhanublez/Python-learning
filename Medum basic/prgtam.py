str=input("Enter string ")
n=len(str)

i=0
while n>0:
    # print(str[i]*int(str[i+1]),end="")
    print(str[i]*int(str[i+1]),end="")
    i=i+2
    n=n-2