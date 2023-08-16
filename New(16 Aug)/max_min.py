#Write a function to find the maximum and
# minimum numbers from a sequence of numbers.
def maxMin(a):
    max=a[0]
    min=a[0]
    for i in a:
        if i>max:
            max=i
        elif i<min:
            min=i
    print("Max hai",max)
    print("Min hai",min)
a=[1,2,3,4,5,6,7,8,9,10]
maxMin(a)