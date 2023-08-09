import csv
#create software.csv file with entries
# https://realpython.com/python-csv/
# https://docs.python.org/3/library/csv.html
with open ('software.csv') as softwater:
    reader = csv.DictReader(softwater)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))    

# Path: dict_writer.py
import csv
#create software.csv file with entries
