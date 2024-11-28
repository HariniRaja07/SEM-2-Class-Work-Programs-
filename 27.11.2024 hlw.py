#1.
class StudentsInfo:
    def __init__(self,name,age,course,grade):
        self.name=name
        self.age=age
        self.course=course
        self.grade=grade
    def display(self):
        print(f"Student details--> Student Name:{self.name}, Age:{self.age},Course:{self.course},Grade:{self.grade}")
    def __del__(self):
        print("The Students details are deleted")
obj1=StudentsInfo("Harini",18,"Artificial Intelligence","A")
obj1.display()

obj2=StudentsInfo("Anu",12,"CS","B")
obj2.display()

del obj1

print("\n")

#2.
class Student:
    def __init__(self):
        self.student_name=input("Enter the Student Name:")
        self.student_rollno=input("Enter the Student Roll No:")
        self.subject1=int(input("Enter your subject 1 mark:"))
        self.subject2=int(input("Enter your subject 2 mark:"))
        self.subject3=int(input("Enter your subject 3 mark:"))
        
    def display(self):
        total=self.subject1+self.subject2+self.subject3
        percentage=(total/300)*100
        if percentage>=85:
            print("Grade:S")
        elif percentage>=75:
            print("Grade:A")
        elif percentage>=65:
            print("Grade:B")
        elif percentage>=55:
            print("Grade:C")
        elif percentage>=50:
            print("Grade:D")
obj1=Student()
obj1.display()
