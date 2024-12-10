#Multi level Inheritance
#1.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayPerson(self):
        print("Name:",self.name,"\nAge:",self.age)
        
class Employee(Person):
    def __init__(self,name,age,Id):
        super().__init__(name,age)
        self.Id=Id
    def display(self):
        self.displayPerson()
        print("ID:",self.Id)

class Manager(Employee):
    def __init__(self,name,age,Id,salary):
        super().__init__(name,age,Id)
        self.salary=salary
    def show(self):
        self.display()
        print("Salary:",self.salary)

obj=Manager("Kamali",60,"E24AI011",100)
obj.show()



#hierarchical Inheritance
#2.
class Person:
    def __init__(self,name,age,Id,course,department):
        self.name=name
        self.age=age
        self.Id=Id
        self.course=course
        self.department=department
    
class Student(Person):
    def __init__(self,name,age,Id,cgpa):
        Person.__init__(self,name,age,Id)
        self.cgpa=cgpa
    def display(self):
        print("Name:",self.name,"Age:",self.age,"Id:",self.Id)
        print("CGPA:",self.cgpa)

class College(Person):
    def __init__(self,course,department,roomno):
        Student.__init__(self,name,age,Id,cgpa)
        self.roomno=roomno
    def show(self):
        print("course:",self.course,"Department:",self.department)
        print("Room No:",self.roomno)

obj=College("Kamali",60,"E24AI017",9,"AI","bsccswithAI","ML4")
obj.show()

