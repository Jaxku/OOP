class Book:
    def __init__(self, title, author, dewey, isbn):
        self.title = title.title()   # String with capitalised first letter
        self.author = author        # String
        self.dewey = dewey          # String
        self.isbn = isbn            # String
        self.available = True
        self.borrower = None
        book_list.append(self)  # Holds book objects as created - main routine

    def book_details(self):
        print(self.title)
        print(self.author)
        print(self.dewey)
        print(self.isbn)
        print(self.available)
        print(self.borrower)
        print("#########################")


# Print list of books
def print_info():
    for book in book_list:
        book.book_details()

#  Main routine
book_list = []

# Create book objects
Book("Lord of the Rings", "J.R.R.Tolkien", "TOL", "9780261103252")
Book("The Hunger Games", "Suzanne Collins", "COL", "9781407132082")
Book("A Tale of Two Cities", "Charles Dickens", "DIC", "9781853262647")
Book("Harry Potter", "J.K.Rowling", "ROW", "9780439321624")

print_info()




