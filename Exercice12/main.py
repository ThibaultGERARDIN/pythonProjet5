class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:

    def __init__(self):
        self.books = []
        self.borrow_books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrow_books.append(book)

    def return_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.borrow_books.remove(book)
                self.books.append(book)

    def available_books(self):
        print("Liste des livres disponibles :\n")
        for book in self.books:
            print(f"{book.title}\n")

    def borrowed_books(self):
        print("Liste des livres empruntés :\n")
        for book in self.borrow_books:
            print(f"{book.title}\n")


book_one = Book("Le Seigneur des Anneaux", "Tolkien", "1960")
book_two = Book("Narnia", "Inconnu", "1990")
book_three = Book("Harry Potter", "JK ROWLING", "1992")
book_four = Book("One Piece", "Eichiiro Oda", "1997")

library = Library()

library.available_books()
library.borrowed_books()
library.add_book(book_one)
library.add_book(book_two)
library.add_book(book_three)
library.add_book(book_four)
library.available_books()
library.borrow_book("Harry Potter")
library.available_books()
library.borrowed_books()
library.remove_book("Narnia")
library.available_books()
library.borrow_book("One Piece")
library.available_books()
library.borrowed_books()
library.return_book("Harry Potter")
library.available_books()
library.borrowed_books()
