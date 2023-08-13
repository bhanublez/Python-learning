import os
f=open('word.txt','w')
f.write("Hava ")
f.write("Dava ")
f.close()
# f=file('word.txt','r')
# for line in f:
#     print(line)
file=open('word.txt')
line=file.readlines()
file.close()
line.sort()
print(line)



