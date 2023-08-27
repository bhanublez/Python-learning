import re
print(re.split(r"[.?!]","One sentence. Another sentence? and last one!"))


print(re.split(r"([.?!])","One sentence. Another sentence? and last one!"))

## Sub Method

print(re.sub(r"[\w.%+-]+@[\w.-]+","[REDACTED]","get email go_nuto86@my.email.com"))
print(re.sub(r"^([\w .-]*), ([\w .-]*)$",r"\2 \1","Lovan, sovan"))
