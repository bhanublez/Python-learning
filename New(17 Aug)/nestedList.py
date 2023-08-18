#Write a program to flat a nested list
# input: [1,2,[3,4,[5,6]],7,8,[9,[10]]]
# output: [1,2,3,4,5,6,7,8,9,10]


# def fun(list,result,i):
#     if(len(list)==0):
#         return result
#     if(list[i]==list):
#         return fun(list.pop,result,0)
#     else:
#         result.append(list.pop(),i+1)
    # while(len(list)>0 and type(list[0])==int ):
    #     result.append(list.pop())
    #     print(result)
    # return fun(list.pop,result,i)
    
    # if(len(list)==0) return 
    # while():
    #     result.append(i)
    #     print(result[i])
    #     i+1
    # else:
    #     return fun(list,result,i+1)
    
    # return result

# d=fun(list,d)
# print(d)

list=[1,2,[3,4,[5,6]],7,8,[9,[10]]]
d=[]

def flatlets(l):
    for i in l:
        if(type(i) == list):
             flatlets(i)
        else:
            d.append(i)

flatlets(list)
print(d)
