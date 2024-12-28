class Student:
    def __init__(self,name,age,dept,cgpa,position):
        self.name=name
        self.age=age
        self.dept=dept
        self.cgpa=cgpa
        self.position=position
    def display(self):
        print("student Details:",self.name,self.age,self.dept,self.cgpa)
    def position(self):
        print("Position:",self.position)

class Person(Student):
    def display(self):
        print("person Details:",self.name,self.age,self.dept,self.cgpa)
    def position(self):
        print("Position:",self.position)

p=Person("Harini",18,"AI",10,"Union Secretary")
s=Student("Abinaya",60,"BSC",10,"chef")

p.display()
p.position()


s.display()
s.position()
