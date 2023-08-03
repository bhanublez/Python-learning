x={}
print(type(x))

#It based on key and value pair concept
file_counts={"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)

print(file_counts["txt"])
print("html" in file_counts)
print("html" not in file_counts)

file_counts["cfg"]=8
print(file_counts)

del file_counts["cfg"]
print(file_counts)

#For loop in dictionary
for extension in file_counts:
    print(extension)

for a,b in file_counts.items():
    print("There are {} files with the .{} extension".format(b,a))

#dicrionary_name.keys() and dictionary_name.values()

