list=[2,3,5,6,10,5]
i=0
j=1
d=[]


def checkInc(d):
    j=0
    for i in d:
        if(not i>=d[j]):
            flag=False
            break
        j=j+1
    else:
        return True
    

def checkDec(d):
    j=0
    for i in d:
        if(not i<=d[j]):
            return False
            break
        j=j+1
    else:
        return True
         

while(i<len(list) and j<len(list)):
    d.append(abs(list[j]-list[i]))
    i=i+1
    j=j+1
print("List is Increasing {}".format(bool(checkInc(d))))

print("List is Decreasing {}".format(bool(checkDec(d))))


