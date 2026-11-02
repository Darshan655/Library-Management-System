"""
Library Management System - Core Module
"""

class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __repr__(self):
        status = "Available" if self.available else "Borrowed"
        return f"[{self.book_id}] '{self.title}' by {self.author} ({status})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.books.append(book)
        print(f"Book added: {book}")
        return book

    def list_books(self):
        return self.books

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print(f"Book '{book.title}' borrowed successfully.")
                    return True
                else:
                    print(f"Book '{book.title}' is already borrowed.")
                    return False
        print(f"Book with ID {book_id} not found.")
        return False

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print(f"Book '{book.title}' returned successfully.")
                    return True
                else:
                    print(f"Book '{book.title}' was not borrowed.")
                    return False
        print(f"Book with ID {book_id} not found.")
        return False


if __name__ == "__main__":
    print("=== Initializing Library Management System ===")
    library = Library()
    
    # Adding initial books
    library.add_book(101, "The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book(102, "To Kill a Mockingbird", "Harper Lee")
    library.add_book(103, "1984", "George Orwell")

    print("\nListing all books:")
    for b in library.list_books():
        print("  -", b)

    print("\nBorrowing book 102:")
    library.borrow_book(102)

    print("\nReturning book 102:")
    library.return_book(102)
