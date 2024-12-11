#1.Encapsulation(using private)
class Student:
    def __init__(self,name,age,department):
        self.__name=name
        self.age=age
        self.department=department
    def show(self):
        print(f"Name: {self.__name}\nAge: {self.age}\nDepartment: {self.department}")
s=Student("kamali",60,"AI")
s.show()

#2.encapsulation(using private)
class Student:
    __id=123
    def __init__(self,name):
        self.__name=name
    def display(self):
        print("Name:",self.__name)
s=Student("Harini Raja")
s.display()
print(s.name)
print(s.id)


#3.encapsulation
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

emp=Employee("Harini",1000000)
print(f"Name: {emp.name}")
print(f"Salary: {emp._Employee__salary}")   #-->this is the way to access private variable outside the class
#accessing the varibles of private outside the class without method
#(obj name dot followed by single underscore class name double underscore variable)

#4.
class studet
