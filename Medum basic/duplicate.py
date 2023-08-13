#Write a prgram remove duplicate element from string
str=[1,2,3,4,4,5,5]
j=[]
for i in str:
    if i not in j:
        j.append(i)
print(j)