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


class User:
    def __init__(self, name, address):
        self.name = name    # String
        self.address = address  # String
        self.fees = 0.00  # Float
        self.borrowed_books = []  # List
        user_list.append(self)  # Holds user objects as created - main routine

    def user_details(self):
        print("Name: ", self.name)
        print("Address: ", self.address)
        print("Fees $", self.fees)
        print("#########################")


# Print list of users
def print_user():
    for user in user_list:
        user.user_details()


# Add a new library user
def add_user():
    name = input("Enter the new user's name: ").title()
    address = input("Enter the new user's address: ")
    User(name, address)
    print(name, address,"Has been added to the user list")


# ADd a new book
def add_book():
    title = input("Enter the new book's title: ").title()
    author = input("Enter the new book's author: ").title()
    dewey = input("Enter the new book's dewey: ").upper()
    isbn = input("Enter the new book's isbn: ")
    Book(title, author, dewey, isbn)
    print(title, author, "Has been added to the book list")


# Find a user
def find_user():
    user_to_find = input("Enter the user's name: ").title()
    for user in user_list:
        if user.name == user_to_find:
            print(f"Hi {user_to_find}")
            return user
    print("Sorry, no user was found with that name")
    return None

#  Main routine
book_list = []
user_list = []

# Create book objects
Book("Lord of the Rings", "J.R.R.Tolkien", "TOL", "9780261103252")
Book("The Hunger Games", "Suzanne Collins", "COL", "9781407132082")
Book("A Tale of Two Cities", "Charles Dickens", "DIC", "9781853262647")
Book("Harry Potter", "J.K.Rowling", "ROW", "9780439321624")

# Create objects - Books
User("John", "12 Example St")
User("Susan", "1011 Binary Rd")
User("Paul", "25 Appletree Dr")
User("Mary", "8 Moon Cres")

add_book()
print_info()
# add_user()
# print_user()





