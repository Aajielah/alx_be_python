class Book:
    def __init__(self, title, author):
        self.title = title          # public
        self.author = author        # public
        self._is_checked_out = False   # private (by convention)

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []   # private list of Book objects

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
                return

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
