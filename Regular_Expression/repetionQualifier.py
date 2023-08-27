import re
print(re.search(r"[a-zA-Z]{5}","a ghost"))
print(re.search(r"[a-zA-Z]{5}","a scary ugly ghost run behind a person to fart on his or her face"))
print(re.findall(r"[a-zA-Z]{5}","a scary ugly ghost run behind a person to fart on his or her face"))

## use of \b to search at fixed mentioned length
print(re.findall(r"\b[a-zA-Z]{5}\b",'A scary ghost farts'))
#Allocating range 
print(re.findall(r"\w{5,10}","I really hate going my college as its to boring"))

print(re.findall(r"s\w{,20}","I loves strawberrieses"))