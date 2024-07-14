class Book:
  """Represents a book in the library."""

  def __init__(self, title, author):
    """Initializes a Book object with title and author.

    Args:
      title: The title of the book (string).
      author: The author of the book (string).
    """
    self.title = title
    self.author = author
    self._is_checked_out = False  # Private attribute to track availability

  def __str__(self):
    """Returns a string representation of the book."""
    return f"{self.title} by {self.author}"

class Library:
  """Represents a library that manages a collection of books."""

  def __init__(self):
    """Initializes a Library object with an empty list of books."""
    self._books = []

  def add_book(self, book):
    """Adds a book object to the library's collection.

    Args:
      book: A Book object to be added.
    """
    self._books.append(book)

  def check_out_book(self, title):
    """Attempts to check out a book by title.

    Args:
      title: The title of the book to check out (string).

    Returns:
      True if the book is successfully checked out, False otherwise.
    """
    for book in self._books:
      if book.title == title and not book._is_checked_out:
        book._is_checked_out = True
        return True
    return False

  def return_book(self, title):
    """Attempts to return a book by title.

    Args:
      title: The title of the book to return (string).

    Returns:
      True if the book is successfully returned, False otherwise.
    """
    for book in self._books:
      if book.title == title and book._is_checked_out:
        book._is_checked_out = False
        return True
    return False

  def list_available_books(self):
    """Returns a list of titles of all available books."""
    available_books = []
    for book in self._books:
      if not book._is_checked_out:
        available_books.append(book.title)
    return available_books
