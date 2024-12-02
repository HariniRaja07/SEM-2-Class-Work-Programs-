#1.
class Library:
    def __init__(self,book_name,author):
        self.book_name=book_name
        self.author=author
    def show(self):
        print(f"{self.book_name}--->{self.author}")
class Member:
    def __init__(self,member_name,access_id,phone_no):
        self.member_name=member_name
        self.access_id=access_id
        self.phone_no=phone_no
    def display(self):
        print(f"{self.member_name} , {self.access_id} , {self.phone_no}")
class Library_management(Library,Member):
    def __init__(self,book_name,author,member_name,access_id,phone_no):
        Library.__init__(self,book_name,author)
        Member.__init__(self,member_name,access_id,phone_no)
    def showInfo(self):
        self.show()
        self.display()
        print(f"The name of the book:{self.book_name}--->taken by {self.member_name}")
obj=Library_management("Unsung king","Demonty","Ragavan","lib123409","8709652143")
obj.showInfo()


#2.
class Restaurant:
    def __init__(self,name,food):
        self.name=name
        self.food=food
    def show(self):
        print(f"{self.name}--->{self.food}")
class Delivery:
    def __init__(self,client_name,contact_no,address,delivery_person,phone_no):
        self.client_name=client_name
        self.contact_no=contact_no
        self.address=address
        self.delivery_person=delivery_person
        self.phone_no=phone_no
    def display(self):
        print(f"Delivery details:{self.client_name} , {self.contact_no} , {self.phone_no}")
class Food_delivery_system(Restaurant,Delivery):
    def __init__(self,name,food,client_name,contact_no,address,delivery_person,phone_no):
        Restaurant.__init__(self,name,food)
        Delivery.__init__(self,client_name,contact_no,address,delivery_person,phone_no)
    def showInfo(self):
        self.show()
        self.display()
obj=Food_delivery_system("Sangeetha","Biryani","Harini","8709652143","pasumpon nagar","Karthik","8925626729")
obj.showInfo()
