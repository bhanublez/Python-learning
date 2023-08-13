#input: B4A1D3
#output: ABD134

#sort in such a manner that all the alphabets are in uppercase and
# he numbers are in ascending order

str=input("Enter the string: ")
alpha=""
num=""
for i in str:
    if i.isalpha():
        alpha=alpha+i
    else:
        num=num+i
alpha=sorted(alpha)
num=sorted(num)
for i in alpha:
    print(i,end="")
for i in num:
    print(i,end="")
