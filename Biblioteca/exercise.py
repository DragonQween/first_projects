class Book:
    def __init__(self, id_book, author, book_name):
        self.id_book = id_book
        self.author = author
        self.book_name = book_name
        self.borrowed = False

    def __str__(self):
        return f"Book({self.id_book}, {self.author}, {self.book_name})"
    
    def __repr__(self):
        return self.__str__()

class Bookshelf:

    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.id_book not in self.books:
            self.books[book.id_book] = book
        else:
            print(f"\n[!] It is not possible to add the book with the following ID: {book.id_book}")

    def borrow_book(self, id_book):
        if id_book in self.books and not self.books[id_book].borrowed:
            self.books[id_book].borrowed = True
        else:
            print(f"\n[!] No books with ID {id_book} available.")

    @property
    def show_books(self):
        return [book for book in self.books.values() if not book.borrowed]

    @property
    def show_borrowed_books(self):
        return [book for book in self.books.values() if book.borrowed]

class Age_restricted(Bookshelf):

    def __init__(self):
        super().__init__()
        self.age_restricted = {}

    def add_book(self, book, age_restricted):
        super().add_book(book)
        self.age_restricted[book.id_book] = age_restricted

    def borrow_book(self, id_book, age_restricted):
        if id_book in self.books and self.age_restricted[id_book] == age_restricted and not self.books[id_book].borrowed:
            self.books[id_book].borrowed = True
        else:
            print(f"\n[!] No books with ID {id_book} available.")

if __name__ == '__main__':

    bookshelf = Age_restricted()

    book1 = Book(1, "Angel David Revilla", "Luna de Pluton")
    book2 = Book(2, "Marcelo Vazquez", "Como ser un Lammer")
    book3 = Book(3, "Courtney Alameda", "The Dragon's War")
    book4 = Book(4, "Stephen King", "Holly")

    bookshelf.add_book(book1, age_restricted=False)
    bookshelf.add_book(book2, age_restricted=False)
    bookshelf.add_book(book3, age_restricted=False)
    bookshelf.add_book(book4, age_restricted=True)

    # Para verificar que los libros fueron añadidos correctamente
    # for id_book, book in bookshelf.books.items():
    #     print(book)

    print(f"\n[+] Library books: {bookshelf.show_books}")

    bookshelf.borrow_book(1, age_restricted=False)

    print(f"\n[+] Library books: {bookshelf.show_books}")
    print(f"\n[+] Borrowed books: {bookshelf.show_borrowed_books}")
