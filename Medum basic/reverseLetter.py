# s="Python is  very easy"
#"output: easy very is Python"
# s=s.split()
# print(" ".join(reversed(s)))

#output: "nohtyP si yrev ysae"
# s=s.split()
# for i in s:
#     print(i[::-1],end=" ")

#alternative method
# p="Python is  very easy"
# p=p.split()
# for i in p:
#     print("".join(reversed(i)),end=" ")

#reversing s string even postion word
s="Python is  very easy"
s=s.split()
j=1
for i in s:
    if j%2==0:
        print("".join(reversed(i)),end=" ")
    else:
        print(i,end=" ")
    j+=1
