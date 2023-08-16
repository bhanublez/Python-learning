#You need to create a program that enter name and marks in dictionary 
#Diplay on screen and store value directly in txt file
record={}
n=int(input("enter number of student: "))
for i in range(n):
    name=input("enter name: ")
    marks=input("Enter marks: ")
    record[name]=marks
    with open("record.txt","a") as f:
        f.write(name+" ")
        f.write(marks)
        f.write("\n")
#record.setdefault(name,marks)