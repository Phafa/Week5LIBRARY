class Universal:
    def __init__(self, title, author, isbn, avilability__status, username, user_id):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.avilability_status = avilability_status
        self.user_name = user_name
        self.user_id = user_id
class Books(Universal):
    def __init__(self, title, author, isbn, avilability_status):   

    def display_book(self):
        return f"the book {self.title} by {self.author}"

    def avilability__status(self):
        if title is not []:
            print('The Book your trying to reach is not avilable')
class User(Universal):

    def __init__(self, user_name, user_id, books_borrowed):
        self.books_borrowed = books_borrowed
    
    def user_info(self):
        return f'user details: {self.user_name}, {user_id}'
    
    def user_status(self):
        if self.books_borrowed is books.avilability_status():
            print('returned')
        else:
            print('borrowed')

class Library(Universal):

    def __init__(self, collectino_books, user_data):
        
        self.collectino_books = collectino_books
        self.user_data = user_data

    def add_book(self):
        collectino_books[]
        self.title = input("Enter a book Title: ")
        self.author = input("Enter Author Name: ")
        self.isbn = input("Enter Isbn: ")
        collectino_books.append(self.title, self.author, self.isbn)
        print("added!!!!")         
    
    def regestr_new_user(self):
        user_data[]
        self.username = input("Enter UserName: ")
        self.user_id = input('Enter Id: ')
        user_data.append(self.username, self.user_id)

    def transaction(self):



class Transaction:

    def __init__(self, borrowing, returning):

        self.borrowing = borrowing
        self.returning = returning

    def record_transaction(self):
        borrowing[]
        self.title = input("Enter The Title: ")

        borrowing.append(self.title)
        print('recorded!!')
        
    def generat_transaction_report(self):
        if borrowing is True:
            print(record_transaction())
        


        



