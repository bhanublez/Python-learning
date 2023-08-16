#Write a binary search function which searches an item in a sorted list. Function should return the index of element to be searched in the list.
def search(list):
    print("Targeted number dena:")
    n=int(input())
    #brute force
    # if n in list:
    #     print("Number is present at ",list.index(n))
    # else:
    #     print("Target number nahi hai")
   
    #binary search
    l=0
    h=len(list)-1
    mid=0
    flag=False
    while l<=h:
        mid=l+(h-l)//2
        if list[mid]<n:
            l=mid+1
        elif list[mid]>n:
            h=mid-1
        else:
            print("Number is present at ",mid)
            flag=True
            break
    if(flag==False):
        print("Targeted value not founded")

list=[1,2,3,4,5,6,7,8,9]
search(list)