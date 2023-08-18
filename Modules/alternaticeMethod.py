l=[]
with open('stupids.txt','r+') as f:
    for i in f:
        l.append(str(i).replace("gems","good"))
    f.truncate(0)
    f.seek(0)
    f.writelines(l)
    f.close()

