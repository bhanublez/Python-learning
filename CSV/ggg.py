#csv full form is comma seperated values
#csv is a file format that is used to store data in a tabular format
#csv files are plain text files that use specific structuring to arrange tabular data
#csv files use commas to seperate columns and new line characters to seperate rows
#csv files are used to store a large number of variables or large amount of data
#csv files are commonly used to transfer data from one database or spreadsheet format to another
import csv

f=open("csv_file.txt")
csv_f=csv.reader(f)
for row in csv_f:
    name,phone,comment=row
    print("name:{},phone:{},comment:{}".format(name,phone,comment))