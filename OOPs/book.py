class Book:
    def __init__(self,Book_No,Book_title,Book_Price):
        self.Book_No=Book_No
        self.Book_title=Book_title
        self.Book_Price=Book_Price

    def totalCost(self,n):
        self.totalCost=n*self.Book_Price
    
    def bookDetail(self):
        print("Book No is {}, book_title is {} and Book_price is {}".format(self.Book_No,self.Book_title,self.Book_Price))
    
    def purchase(self,n):
        n=int(input("Enter the number of books copies to be purchase"))
        totalCost(n)
        print("Toatal cost of Book is ",self.totalCost)

b1=Book(1001,"Beauty in Beast",100)
b1.purchase(10)



