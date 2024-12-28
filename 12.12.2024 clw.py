import random
class Customer:
    def __init__(self,customer_id,name,phone_no):
        self.customer_id=customer_id
        self.name=name
        self.phone_no=phone_no
    def generate_customer_id(self):
        c_id=random.randint(1000,9999)
        return f"TICK{c_id}"
    def verify_customer_id(self,customer_id):
        if customer_id[0:3]=="TICK" and customer_id[4:7].isdigit:
            print("it is verify")
        else:
            print("It is not verify")

class TicketBooking:
    def __init__(self):
        self.events={"Concert":{"price":1000,"seats":2000},"Movie":{"price":500,"seats":1000},"Drama":{"price":300,"seats":600},"Restaurant":{"price":250,"seats":100}}
        self.booked_tickets=[]
        
    def view_events(self):
        for events,details in self.events.items():
            print(f"{events}:{details['price']}per tickets {details['seats'])} seats are available")
        
    def book_tickets():

    def view_tickets():
        

book=TicketBooking()

print("**********WELCOME TO TICKET BOOKING APPLICATION**********")
customer_id=input("Enter the customer Id:")

if Customer.verify_customer_id(customer_id):
    name=input("Enter you name:")
    phone_no=int(input("Enter your phone number:"))
    customer=Customer(customer_id,name,phone_no)
    print("*****Booking Details*****")
else:
    print("*****Please Register*****")
    name=input("Enter your name:")
    phone_no=int(input("Enter your phone number:"))
    customer_id=Customer.generate_customer_id()
    customer=Customer(customer_id,name,phone_no)
    print("your Customer Id is:",customer_id

while True:
    print("*****Booking Info*****")
    print("\n1.View My Events")
    print("\n2.Book Tickets")
    print("\n3.View my tickets")
    print("\n4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        book.view_events()
    elif choice==2:
        event_name=input("Enter any event:")
        quantity=input
        book.book_tickets(event_name,quantity)
    elif choice==3:
        book.view_tickets()
    elif choice==4:
        exit()
    else:
        print("Invalid Choice")
