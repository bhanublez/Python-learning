#basic command line in pytho
from sys import argv
print(type(argv))
print(argv)
#insertion in argv
argv.insert(1,1)
argv.insert(2,2)
argv.insert(3,3)
argv.insert(4,4)
print(argv)
#addtion of argv value
# print(int(argv[1])+int(argv[2])+int(argv[3])+int(argv[4]))
sum=0
for i in range(1,len(argv)):
    sum=sum+int(argv[i])
print(sum)

a=argv[1]
b=argv[2]
print(int(a)+int(b))
#List unpacking in python is done when we have a list of values on left
#side of assignment operator
# and we need to unpack the values to variables on right side.

a,b,c=[12,23,345]
print(a,b,c)

#Sperator attribute in print function
print(a,b,c,sep=",")

#end attribute in print function
print(a,end="#")
print(b,end="#")
print(c,end="#")

#format attribute in print function
print()
print("a={0} b={1} c={2}".format(a,b,c))

#print function with formated String
a,b,c,d,e=[12,23.5,"RAJ",{1:"danva"},(1,2,3,4,5)]
print("It is int value is %i or %d"%(a,a))
print("It is float value is %f or %F"%(b,b))
print("It is string value is %s "%(c))
print("It is dictionary value is %r"%(d))
print("It is tuple value is %d and %r"%(a,e))

# f string
print(f"It is int value is {a} or {a}")

print(f"it is {e}")
