import csv
from datetime import date
#  books.py includes [Book_id, Book_name, Author, Type, Issued_to, Issued_on]
def display_books():
    print("\033c")
    print("Displaying all books: \n ")
    try:
        with open("books.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 0 :
                    if row[4] != None and row[5] != None:
                        print("Book_id: {}  Book_name: {}  Author_name:  {}  Book_Type: {}  Issued_To: {} Issued_on: {}".format( row[0], row[1], row[2], row[3],row[4],row[5]))
                    else:
                        print("Book_id: {}  Book_name: {}  Author_name:  {}  Book_Type: {}  Issued_To: {} Issued_on: {}".format( row[0], row[1], row[2], row[3], "None", "None"))
            input("\n \n")
        
    except:
        print("File hi nahi mili bhai ya kuch toh gad bade hai \n")
        input("Kuch bhi type karo for main menu: ")

def add_books():
    print("\033c")
    print("Adding books: \n")
    while True:
        try:
            book_id = int(input("Enter book id: "))
            book_name = input("Enter book name: ")
            author = input("Enter author name: ")
            book_type = input("Enter book type: ")
            with open("books.csv", "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([book_id, book_name, author, book_type, None, None])
                
            print("Book added successfully \n")
            input("Kuch bhi type karo for main menu:")
            break 
        except:
            retry = input("Kuck bhi type karo for re entry: ")
            add_books()

def modify_books():
    print("\033c")
    print("Modifying books: \n")
    
    try:
        book_id = int(input("Enter book id: "))
        with open("books.csv", "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
            for row in rows:
                if len(row) > 0 and int(row[0]) == book_id:
                    book_name = input("Enter book name: ")
                    author = input("Enter author name: ") 
                    book_type = input("Enter book type: ")
                    row[1] = book_name
                    row[2] = author
                    row[3] = book_type
                    break
        with open("books.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            print("Book modified successfully")
            
    except:
        print("File hi nahi mili bhai ya kuch toh gad bade hai \n")
        
    input("")


def delete_books():
    print("\033c")
    print("Deleting books: \n")
    
    try:
        book_id = int(input("Enter book id: "))
        ikata = []
        with open("books.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 0 and int(row[0]) != book_id:
                    ikata.append(row)
        with open("books.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(ikata)
            print("Book deleted successfully")
            
    except:
        print("File hi nahi mili bhai ya kuch toh gad bade hai \n") 
    input()

def search_books():
    print("\033c")
    print("Searching books: \n ")
    try:
        with open("books.csv", "r") as file:
            reader = csv.reader(file)
            book_id = input("Enter book id: ")
            for row in reader:
                if(len(row) > 0):
                    if len(row) > 0:
                        if row[0] == book_id:
                            print(row)
                            break
            print("No yeah book nahi hai")
    except:
        print("File hi nahi mili bhai ya kuch toh gad bade hai \n")
    input()

# Path: users.py [User_id, User_name, User_contact, email, Issued_books]
def display_users():
    print("\033c")
    print("Displaying all users: ")
    try:
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except:
        print("File hi nahi mili bhai ya kuch toh gad bade hai \n")
    input()

def add_users():
    print("\033c")
    print("Adding users: ")
    try:
        with open("users.csv", "a") as file:
            writer = csv.writer(file)
            user_id = int(input("Enter user id: "))
            user_name = input("Enter user name: ")
            user_contact = int(input("Enter user contact: "))
            email = input("Enter email: ")
            # issued_books = list(int(input("Enter issued books: ").split(",")))
            writer.writerow([user_id, user_name, user_contact, email, None])
            print("User added successfully")
    except:
        print("File hi nahi mili bhai ya kuch toh gad bade hai \n")
    input()

def modify_users():
    print("\033c")
    print("Modifying users: \n")
    try:
        user_id = int(input("Enter user id: "))
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
            for row in rows:
                if len(row) > 0 and int(row[0]) == user_id:
                    user_name = input("Enter user name: ")
                    user_contact = input("Enter user contact: ")
                    email = input("Enter email: ")
                    issued_books = input("Enter issued books: ")
                    row[1] = user_name
                    row[2] = user_contact
                    row[3] = email
                    row[4] = issued_books
                    break
        with open("users.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            print("User modified successfully")
    except:
        print("File hi nahi mili bhai ya kuch toh gad bade hai \n")
    input()

def delete_users():
    print("\033c")
    print("Deleting users: \n")
    
    try:
        user_id = input("Enter user id: ")
        rows_to_keep = []
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 0 and int(row[0]) != int(user_id): 
                    rows_to_keep.append(row)
        with open("users.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows_to_keep)
            print("User deleted successfully")
            
    except:
        print("File hi nahi mili bhai ya kuch toh gad bade hai \n")
        
    input()

def search_users():
    print("\033c")
    print("Searching users: \n")
    try:
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            user_id = int(input("Enter user id: "))
            for row in reader:
                if(len(row) > 0):
                    if int(row[0]) == user_id:
                        print("Yes Yeah Bacha hai")
                        break
            print("No yeah bacha nahi hai")
    except:
        print("File hi nahi mili bhai ya kuch toh gad bade hai \n")
    input()

def issue_books():
    print("\033c")
    print("Issuing books: \n")
    
    try:
        user_id = int(input("Enter user id: "))
        book_id = int(input("Enter book id: "))
        with open("books.csv", "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
            for row in rows:
                if int(row[0]) == book_id:
                    row[4] = str(user_id) 
                    row[5] = str(date.today()) 
                    break
        with open("books.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
            for row in rows:
                if int(row[0]) == user_id:
                    issued_books = row[4].split(',')  
                    issued_books.append(str(book_id))  
                    row[4] = ','.join(issued_books)  
                    break
        with open("users.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            print("Book issued successfully")
        
    except:
        print("File hi nahi mili bhai ya kuch toh gad bade hai \n")
        
    input()

def return_books():
    print("\033c")
    print("Returning books: \n")
    
    try:
        book_id = input("Enter book id: ")
        
        # Update the book's issued user and date
        with open("books.csv", "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
            for row in rows:
                if row[0] == book_id:
                    row[4] = ""  
                    row[5] = ""  
                    break
        with open("books.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            print("Book returned successfully")
        
        user_id = input("Enter user id: ")
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
            for row in rows:
                if row[0] == user_id:
                    issued_books = row[4].split(',')
                    issued_books.remove(book_id)
                    row[4] = ','.join(issued_books)
                    break
        with open("users.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        
    except ValueError:
        print("Invalid input. Please enter a valid ID.")
    except:
        print("File hi nahi mili bhai ya kuch toh gad bade hai \n")
    input()

def launch():
    while(True):
        print("\033c")
        print("Welcome to SISTEC Library: \n")
        print("Choose from the following below operations: ")
        print("1. Display all Books")
        print("2. Add books")
        print("3. Modify books")
        print("4. Delete books")
        print("5. Show Users")
        print("6. Add Users")
        print("7. Modify Users")
        print("8. Delete Users")
        print("9. Issue Books")
        print("10. Return Books")
        print("11. Search Books")
        print("12. Search Users")
        print("13. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            display_books()
        elif choice == 2:
            add_books()
        elif choice == 3:
            modify_books()
        elif choice == 4:
            delete_books()
        elif choice == 5:
            display_users()
        elif choice == 6:
            add_users()
        elif choice == 7:
            modify_users()
        elif choice == 8:
            delete_users()
        elif choice == 9:
            issue_books()
        elif choice == 10:
            return_books()
        elif choice == 11:
            search_books()
        elif choice == 12:
            search_users()
        elif choice == 13:
            print("Thank you for using SISTEC Library")
            break
        else:
            print("Invalid choice")
            input("Kuch bhi type karo for re entry at main menu: ")

launch()
