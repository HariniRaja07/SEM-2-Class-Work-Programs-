#1.
class BankAccount:
    def __init__(self,holder_name,account_no,balance):
        self.holder_name=holder_name
        self.account_no=account_no
        self.balance=balance
    def deposit_money(self,amount):
        if amount>0:
            self.balance+=amount
            print("The amount after deposited :",self.balance)
    def withdraw_money(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("The amount after withdraw :",self.balance)
        else:
            print("The account balance is insufficient to withdraw the money")
            
    def display(self):
        print("Account Holder Name:",self.holder_name)
        print("Account Number:",self.account_no)
        print("Balance amount in your Account:",self.balance)
obj1=BankAccount("Harini Raja","24350687910",3000)
obj1.display()
obj1.deposit_money(10000)
obj1.withdraw_money(10000)



#2.
class Cosmetic:
    def __init__(self,product_name="Foundation",brand="Lakme",price=400,category="Face Cream"):
        self.product_name=product_name                                     
        self.brand=brand
        self.price=price
        self.category=category
    def display(self):
        print("Product Name:",self.product_name)
        print("Brand:",self.brand)
        print("Cost:",self.price)
        print("Category:",self.category)
obj=Cosmetic()   
obj.display()

