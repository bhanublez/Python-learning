multiple=[]
for x in range(1,11):
    multiple.append(x*7)
print(multiple)

#The othe comprehension list method
print([x*7 for x in range(1,11)])

length=["one","twoo","three","fourss","fiveeee"]
length=[len(x) for x in length]
print(length)