class Book:
    def __init__(self, title , author):
        self.title = title
        self.author = author
    def __str__(self):
        print(f"Book: {self.title} by {self.author}")
    
class EBook(Book):
    def __init__(self, file_size):
        Book.__init__(self, file_size)
        self.file_size = file_size
    def __str__(self):
        print(f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB")
class PrintBook(Book):
    def __init__(self, page_count):
        Book.__init__(self, page_count)
        self.page_count = page_count
    def __str__(self):
        print(f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}")
class Library:
    pass


