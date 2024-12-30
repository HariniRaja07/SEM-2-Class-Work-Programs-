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
        if customer_id[0]=="T" and customer_id[1]=="I" and customer_id[2]=="C" and customer_id[3]=="K" and customer_id[4].isdigit() and customer_id[5].isdigit() and customer_id[6].isdigit() and customer_id[7].isdigit():
            print("it is verify")
        else:
            print("It is not verify")


print("**********WELCOME TO TICKET BOOKING APPLICATION**********")
customer_id=input("Enter:")
obj=Customer(customer_id,"Harini",7200217676)
obj.generate_customer_id()
obj.verify_customer_id(customer_id)
