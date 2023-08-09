import os
# print(os.getcwd())
# os.mkdir("newdir")
# os.chdir("newdir")
# print(os.getcwd())
# os.mkdir("newdir2")
# os.rmdir("newdir2")
print(os.listdir("website"))
#output: ['images', 'index.html', 'styles']
dir ='website'
for name in os.listdir(dir): #listing directories
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
