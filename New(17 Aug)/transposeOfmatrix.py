i=[[1,2],[3,4],[5,6]]
d=[]
for j in range(len(i[0])):
    c=[]
    for k in range(len(i)):
        c.append(i[k][j])
    d.append(c)
print(d)
