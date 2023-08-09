def enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1

for i, c in enumerate('abc', 0):
    print(i, c)
    
print()

for i, c in enumerate('abc', 1):
    print(i, c)

