#Class Methods Assignment: Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added

class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    def display_book_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")
book4 = Book("Pride and Prejudice", "Jane Austen")

book1.display_book_info()
book2.display_book_info()
book3.display_book_info()
book4.display_book_info()

print(f"Total number of books: {Book.get_total_books()}")