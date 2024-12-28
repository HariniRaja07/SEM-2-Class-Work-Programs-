#1.
class User:
    def __init__(self, username):
        self.__username = username
        self.__password = None

    def set_password(self, password):
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            return
        if not any(char.isdigit() for char in password):
            print("Password must contain at least one number.")
            return
        if not any(char in "!@#$%^&*(),.?\":{}|<>" for char in password):
            print("Password must contain at least one special character.")
            return
        self.__password = password
        print("Password set successfully.")

    def check_password(self, input_password):
        if input_password == self.__password:
            print("Password is correct.")
            return True
        else:
            print("Password is incorrect.")
            return False

username = input("Enter username: ")
user = User(username)  
password = input("Enter password: ") 
user.set_password(password)

entered_pass = input("Enter password again to check: ")  
user.check_password(entered_pass)


#2.

class Product:
    def __init__(self, name):
        self._name = name
        self._price = 0.0
        self._stock = 0

    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            print("Price must be greater than 0.")

    def set_stock(self, stock):
        if stock==int(stock) and stock >= 0:
            self._stock = stock
        else:
            print("Stock must be a non-negative integer.")

    def get_stock(self):
        return self._stock

name = input("Enter product name: ")
product = Product(name)

price = float(input("Enter product price: "))
product.set_price(price)

stock = int(input("Enter product stock: "))
product.set_stock(stock)

print(f"Current stock of {product._name}: {product.get_stock()}")

#3.

class Student:
    def __init__(self, name, age, marks):
        self._name = name
        self._age = None
        self._marks = None
        self.set_age(age)
        self.set_marks(marks)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if 5 <= age <= 100:
            self._age = age

    def get_marks(self):
        return self._marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks

name=input()
age=int(input())
mark=int(input())
student = Student(name,age,mark)
print(f"Name: {student.get_name()}")
print(f"Age: {student.get_age()}")
print(f"Marks: {student.get_marks()}")


