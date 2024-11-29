#1.
class Person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print("The name of the Person:",self.name)
class Student(Person):
    def getInfo(self,student_id):
        self.show_name()
        self.student_id=student_id
    def show_student_id(self):
        print("The Student ID:",self.student_id)
stu=Student("Harini")
stu.getInfo("E24AI011")
stu.show_student_id()
    
    
#2.
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_details(self):
        print(f"Employee-->{self.name} , {self.salary}")
class Manager(Employee):
    def getInfo(self,department):
        self.display_details()
        self.department=department
    def display_department(self):
        print("The name of the department:",self.department)
emp=Manager("Harini","800000")
emp.getInfo("Software Developer")
emp.display_department()


        



    
        



        
        
