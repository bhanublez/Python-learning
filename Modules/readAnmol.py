def add():
    list=[]
    n=int(input("Enter number of data "))
    for i in range(n):
        list.append(str(input("Enter data: ")))

file=open("anmol.txt",'r+')
# print(file.readlines())
# print("file name",file.name)
# print("file mode",file.mode)
# print("file readable ",file.readable())
# print("file writeable ",file.writable())
# print("file is close ",file.closed)
# print("file is close now ",file.closed)

# readable methods
print(file.read())# read() method read whole file
print(file.tell())# tell() method tells the current position of the file pointer
print(file.read(5))# read(n) method read n characters from the file
print(file.readline(144))# readline() method read one line from the file
print(file.readlines())# readlines() method read all lines from the file and return a list of lines
print(file.seek(0))# seek() method change the current position of the file pointer

file.close()
