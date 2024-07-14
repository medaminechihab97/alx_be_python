# class Book:
#   """Represents a book in the library."""

#   def __init__(self, title, author):
#     """Initializes a Book object with title and author.

#     Args:
#       title: The title of the book (string).
#       author: The author of the book (string).
#     """
#     self.title = title
#     self.author = author
#     self._is_checked_out = False  # Private attribute to track availability

#   def __str__(self):
#     """Returns a string representation of the book."""
#     return f"{self.title} by {self.author}"
#     return_book(self)

# class Library:
#   """Represents a library that manages a collection of books."""

#   def __init__(self):
#     """Initializes a Library object with an empty list of books."""
#     self._books = []

#   def add_book(self, book):
#     """Adds a book object to the library's collection.

#     Args:
#       book: A Book object to be added.
#     """
#     self._books.append(book)

#   def check_out_book(self, title):
#     """Attempts to check out a book by title.

#     Args:
#       title: The title of the book to check out (string).

#     Returns:
#       True if the book is successfully checked out, False otherwise.
#     """
#     for book in self._books:
#       if book.title == title and not book._is_checked_out:
#         book._is_checked_out = True
#         return True
#     return False

#   def return_book(self, title):
#     """Attempts to return a book by title.

#     Args:
#       title: The title of the book to return (string).

#     Returns:
#       True if the book is successfully returned, False otherwise.
#     """
#     for book in self._books:
#       if book.title == title and book._is_checked_out:
#         book._is_checked_out = False
#         return True
#     return False

#   def list_available_books(self):
#     """Returns a list of titles of all available books."""
#     available_books = []
#     for book in self._books:
#       if not book._is_checked_out:
#         available_books.append(book.title)
#     return available_books
from library_management import Book, Library

def test_book_creation():
  """Tests creating a Book object with title and author."""
  book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
  assert book.title == "The Hitchhiker's Guide to the Galaxy"
  assert book.author == "Douglas Adams"

def test_book_string_representation():
  """Tests the string representation of a Book object."""
  book = Book("The Lord of the Rings", "J.R.R. Tolkien")
  assert str(book) == "The Lord of the Rings by J.R.R. Tolkien"

def test_library_add_book():
  """Tests adding a Book object to the Library."""
  library = Library()
  book = Book("The Martian", "Andy Weir")
  library.add_book(book)
  assert len(library._books) == 1  # Check if book is added to internal list

def test_library_check_out_book_success():
  """Tests checking out a book by title (successful case)."""
  library = Library()
  library.add_book(Book("Pride and Prejudice", "Jane Austen"))
  assert library.check_out_book("Pride and Prejudice") == True

def test_library_check_out_book_failure():
  """Tests checking out a book by title (failure case - not found)."""
  library = Library()
  library.add_book(Book("The Catcher in the Rye", "J.D. Salinger"))
  assert library.check_out_book("To Kill a Mockingbird") == False  # Not in library

def test_library_return_book_success():
  """Tests returning a book by title (successful case)."""
  library = Library()
  book = Book("Animal Farm", "George Orwell")
  library.add_book(book)
  library.check_out_book("Animal Farm")
  assert library.return_book("Animal Farm") == True

def test_library_return_book_failure():
  """Tests returning a book by title (failure case - not checked out)."""
  library = Library()
  library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
  assert library.return_book("The Great Gatsby") == False  # Not checked out

def test_library_list_available_books():
  """Tests listing titles of all available books."""
  library = Library()
  library.add_book(Book("Frankenstein", "Mary Shelley"))
  library.add_book(Book("Moby Dick", "Herman Melville"))
  library.check_out_book("Frankenstein")
  available_books = library.list_available_books()
  assert "Moby Dick" in available_books
  assert "Frankenstein" not in available_books

if __name__ == "__main__":
  test_book_creation()
  test_book_string_representation()
  test_library_add_book()
  test_library_check_out_book_success()
  test_library_check_out_book_failure()
  test_library_return_book_success()
  test_library_return_book_failure()
  test_library_list_available_books()
  print("All tests passed!")
