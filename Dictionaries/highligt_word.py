def highlight_word(sentence, word):
    # Complete the return statement using a string method.
    return sentence.replace(word, word.upper())


print(highlight_word("Have a nice day", "nice"))
# Should print: "Have a NICE day"
print(highlight_word("Shhh, don't be so loud!", "loud"))
# Should print: "Shhh, don't be so LOUD!"
print(highlight_word("Automating with Python is fun", "fun"))
# Should print: "Automating with Python is FUN"

genre="transcendental"
print(genre[:-8])