def count_numbers(text):
    result = {}
    # Go through each character in the text
    for character in text:
        # Check if the character is numeric
        if character.isnumeric():
            # Add or increment the value in the dictionary
            if character not in result:
                result[character] = 1
            else:
                result[character] += 1
    return result

print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}

print(count_numbers("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}

print(count_numbers("This is a sentence."))
# Should be {}

print(count_numbers("55 North Center Drive"))
# Should be {'5': 2}
