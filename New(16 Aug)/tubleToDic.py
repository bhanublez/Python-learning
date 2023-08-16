#Write a function which takes a tuple of integer’s values 
#and return a dictionary who’s each item is a pair of integer’s
# values and its frequency.
tub=(1,2,1,1,45,34,5,23,6,3,23,5)
def change(tu):
    dic={}
    for i in tu:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1 

    return dict(sorted(dic.items()))    

print(change(tub))


