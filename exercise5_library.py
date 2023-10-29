""" 
LIBRARY MANAGEMENT:
> Write a Library class with no_of_books and books as two instance variables. 
> Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. 
> Show that your program doesnt persist the books after the program is stopped!
"""
class Library:
    def __init__(self):
        self.num_Of_books = 0
        self.books = []
    def addBook(self, book):
        self.books.append(book)
        self.num_Of_books = len(self.books)
    def showDetails(self):
        print(f"Library has total {self.num_Of_books} books.")
        for i in range(0,len(self.books)):
            print(f"Book No.{i+1} = {self.books[i]}")
        
l1 = Library()
l1.addBook("Harry potter")
l1.addBook("Who will cry when i die")
l1.addBook("John elia")
l1.addBook("Radhe-Krishna")
l1.showDetails()
