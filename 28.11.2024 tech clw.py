#1. just acessing methods in the employee class using inheritance.
class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter the ID:")
        self.name=input("Enter the Name:")
    def display(self):
        print("ID=",self.id,"Name:",self.name)
class Perks(Employee):
    def getdetails(self):
        self.salary=int(input("Enter the salary:"))
    def displayinfo(self):
        print("Salary:",self.salary)
p=Perks()
p.getEmployeeInfo()
p.display()
p.getdetails()
p.displayinfo()


#2.accessing the methods of employee class inside the perks class 
class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter the ID:")
        self.name=input("Enter the Name:")
    def display(self):
        print("ID=",self.id,"Name:",self.name)
class Perks(Employee):
    def getdetails(self):
        self.getEmployeeInfo()
        self.salary=int(input("Enter the salary:"))
    def displayinfo(self):
        self.display()
        print("Salary:",self.salary)
p=Perks()
p.getdetails()
p.displayinfo()

#3.
class Inventory:
    def getDetails(self):
        self.proName=input()
        self.proId=input()
        self.proCost=int(input())
class Product(Inventory):
    def displayDetails(self):
        self.getDetails()
        print("Name of the product:",self.proName)
        print("ID of the product:",self.proId)
        print("Cost of the product:",self.proCost)
pro=Product()
pro.displayDetails()

#4.
class Inventory:
    def getDetails(self):
        self.proName=input()
        self.proId=input()
        self.proCost=int(input())
    def displayDetails(self):
        print("Name of the product:",self.proName)
        print("ID of the product:",self.proId)
        print("Cost of the product:",self.proCost)
pro=Inventory()
pro.getDetails()
pro.displayDetails()


