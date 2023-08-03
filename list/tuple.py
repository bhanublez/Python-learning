#tuple are similar to list but they are immutable
#tuple can be created by using () or tuple() function
#tuple can be accessed by using index

# s=("one","two","three")
# print(s)
#tuple can be accessed by using index
# print(s[0])

def file_size(file_info):
	strinA,strinfB,number = file_info
	return("{:.2f}".format(number / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) 
print(file_size(('Notes', 'txt', 496))) 
print(file_size(('Program', 'py', 1239))) 


