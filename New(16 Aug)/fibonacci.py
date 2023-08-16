#Write a function to generate Fibonacci series for the number 
#input by user. (note implement without recursion)

def fibonacci(n):
    list=[]
    a=0
    b=1
    for i in range(n):
        list.append(a)
        a,b=b,a+b
    return list
n=int(input("Enter the number "))
list=fibonacci(n)
print(list)
