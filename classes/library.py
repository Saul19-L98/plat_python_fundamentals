class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"The book {self.title} has been borrowed.")
        else:
            print(f"This book {self.title} is not available")

    def return_book(self):
        self.available = True
        print(f"The book {self.title} was returned.")
        

class User:
    def __init__(self,name,user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrowed_book(self,book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"The book {book.title} was not available")


    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"The book {book.tile} is not part of the list of borrowed books.")


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self,book):
        self.books.append(book)
        print(f"The book {book.title} was added successfuly.")

    def register_user(self,user):
        self.users.append(user)
        print(f"User {user.name} was added successfuly.")

    def show_available_books(self):
        print("Avaiblable books:")
        for book in self.books:
            if book.available:
                print(f"{book.title} by {book.author}.")


book1 = Book("El principito","Antoine de Saint-Exupéry")
book2 = Book("1984", "George Orwell")

user1 = User("Carli", "001")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_user(user1)

library.show_available_books()

user1.borrowed_book(book1)

library.show_available_books()

user1.return_book(book1)

library.show_available_books()
