#1.
class Library:
    def display_library(self):
        print("Library Name")

class Book(Library):
    def display_book(self):
        print("Book Title")

class Member:
    def display_member(self):
        print("Member Name")

class Transaction(Book, Member):
    def display_transaction(self):
        print("Issue Date ")

K = Transaction()

K.display_library()
K.display_book()
K.display_member()
K.display_transaction()


#2.
class Library:
    def display_library(self):
        print(f"Library Name: {self.name}")

class Book(Library):
    def display_book(self):
        print(f"Book Title: {self.book_title}")

class Member:
    def display_member(self):
        print(f"Member Name: {self.member_name}")

class Transaction(Book, Member):
    def display_transaction(self):
        print(f"Issue Date: {self.issue_date}")
        
s = Transaction()
s.name = "SDNBV Library"
s.book_title = "The Pie and the tart"
s.member_name = "Kamalika"
s.issue_date = "09-12-2024"

s.display_library()
s.display_book()
s.display_member()
s.display_transaction()
