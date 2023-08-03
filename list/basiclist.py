#list is a collection which is ordered and changeable. Allows duplicate members.
#list is mutable i.e. we can change the list elements
#list is represented by square brackets
#list can contain different data types

s=["one","two","three"] #Normal list
type(s)
print(s)

#Accessing list elements
print(s[1])

#Negative indexing
print(s[-1])
#print(s[4]) #IndexError: list index out of range

#list lenght
print(len(s))

#list slicing
print("list slicing example")
print(s[1:3])
print(s[:2])
print(s[1:])

#list append
s.append("four")

#list insert
print("list insert example")
s.insert(1,"one and half")
print(s)
s.insert(0,"zero")
print(s)
s.insert(10,"ten")

#list remove
s.remove("one and half")
print(s)

#list pop
s.pop()
print(s)

#checking list contains or not
print("four" in s)
print("three" in s)

#list reverse
s.reverse()
print(s)

#list sort
s.sort()
print(s)

#list clear
s.clear()
print(s)

#list copy
s=["one","two","three"]
s1=s.copy()
print(s1)

#list extend
s.extend(s1)
print(s)

#list count
print(s.count("one"))

#list index
print(s.index("two"))


#list min
print(min(s))

#list max
print(max(s))

#list sum
#s=["one","two","three"] #TypeError: unsupported operand type(s) for +: 'int' and 'str'
s=[1,2,3]
print(sum(s))

#list element changing
s[0]="ZZEERROO"
print(s)