#Program to display all Postion of subtstring 
#in a given string
str=input("Enter karo string ko: ")
sub=input("Isko find karo: ")
curr=-1
flag=False
n=len(str)
while True:
    curr=str.find(sub,curr+1,n)
    if curr==-1:
        break
    print("Yeah hai ",curr)
    flag=True

if(flag==False):
    print("Kuch Bhi nahi Mila")
