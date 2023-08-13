#In some string there function that are inplace 
#find function is used to find a particular patteren in the string
#find function return the index of the first occurance of the pattern
str="Learning python is very easy"
print(str.find("python"))
print(str.find("python ")+(len("python ")-1))

#find fcunction return -1 if the pattern is not found
print(str.find("bhanu"))
print(str.find("python",1,5))

#Index function is same as find function but it return
#  error if the pattern is not found
print(str.index("python"))