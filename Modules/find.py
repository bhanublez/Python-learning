file=open("anmol.txt","r+")
data=file.read()
print(data)
print("Number of words ",len(data.split()))
count=0
for i in data:
    if(i.isascii):
        count+=1
print("Number of character ",count)
file.seek(0)
print("Number of line ",len(file.readlines()))