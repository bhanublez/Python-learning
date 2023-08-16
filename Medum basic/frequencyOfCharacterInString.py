s=input("Enter the input data bro:")
d={}
for i in s:
    # d[i]=d.get(i,0)+1
    if(i in d.keys()):
        d[i]+=1
    else:
        d[i]=1
# print(d)

for i,j in d.items():
    if(i!=list(d.keys())[-1]):
        print("{}-{}".format(i,j),end=",")
    else:
        print("{}-{}".format(i,j),end="")
#approach two
# s = input("Enter the data : ")
# d = {}
# l = []
# for x in s:
#     if x in d.keys():
#         d[x]=d[x]+1
#     else:
#         d[x]=1
# for k,v in d.items():
#     temp = "{}--{}".format(k,v)
#     l.append(temp)

# print(",".join(l))
