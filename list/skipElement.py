def skip_elements(elements):
    # Initialize variables
    result = []
    i = 0
    for element in elements:
        if i%2 == 0:
            result.append(element)
        i+=1
    return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']