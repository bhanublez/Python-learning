#Write a program to display
# Unique vowels present in the given word
word=input("Enter a word ")
word=word.lower()
vowels="aeiou"
uV=""
for i in word:
    if(i in vowels):
        if(i not in uV):
            uV+=i
print(uV)
