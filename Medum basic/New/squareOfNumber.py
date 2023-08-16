# Write a program which can generate and print a tuple,
# where the values are the squares of number between 
# 1 and 20 (both included)
tuble=()
for i in range(1,21):
    tuble+=(i*i,)
print(tuble)