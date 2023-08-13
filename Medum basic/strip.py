# strip function python
x=input()
print(x.strip())
# strip function removes the spaces from the string
print(x.strip("a"))
print(x.strip("a").strip("b"))
print(x.strip("a").strip("b").strip("c"))
print(x.lstrip("a").rstrip("c"))
