# **Set**

## Introduction

 1. set only take unqie element
 2. In set duplicate are not allowed
 3. set is unordered as in insertion order is not preserved(till 3.6 version)
 4. set is mutable
 5. set is iterable
 6. set is not subscriptable or have inserting heterogenous data allowed

## Creating set

    1. set() # empty set
    2. {1,2,3,4,5}  # set with element
    3. set([1,2,3,4,5]) # set with list
    4. set((1,2,3,4,5)) # set with tuple
    5. set({1,2,3,4,5}) # set with set

## Adding element in set

    1. add()
    2. update()

## Removing element in set
  
        1. remove()
        2. discard()
        3. pop()
        4. clear()

## Some mathematical operation in Set

x={1,2,3,4,5}
y={6,7,8,9,10}
print(x.union(y))
print(x.intersection(y))
print(x.difference(y))

## set comprehension

    1. {i for i in range(10)}
    2. {i for i in range(10) if i%2==0}
    3. {i for i in range(10) if i%2==0 else i*2}

## distinct vowels in set

vowels = set('aeiou')
str=eval(input("Enter data in set: "))
result=set()
for i in str:
    if i in vowels:
        result.add(i)
print(result)

## Frozen Set implementation  

    1. frozenset() # empty frozenset
    2. frozenset({1,2,3,4,5}) # frozenset with element
    3. frozenset([1,2,3,4,5]) # frozenset with list
    4. frozenset((1,2,3,4,5)) # frozenset with tuple
    5. frozenset({1,2,3,4,5}) # frozenset with set
