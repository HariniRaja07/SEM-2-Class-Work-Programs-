class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def validate_name(self):
        if self.name.isupper() and self.name.isalpha():
            print("The Name is Valid")
        else:
            raise ValueError("Invalid Name")
            
    def validate_mark(self):
        if 0<self.mark<100:
            print("The mark is valid")
        else:
            raise ValueError("Invalid Mark")
    def calculate_grade(self):
        if 90<=self.mark<=100:
            print("Grade A")
        elif 80<=self.mark<=89:
            print("Grade B")
        elif 70<=self.mark<=79:
            print("Grade C")
        elif 60<=self.mark<=69:
            print("Grade D")
        else:
            print("Grade F")

try:
    n=input("Enter a name:")
    m=int(input("Enter a mark:"))
    s=Student(n,m)
    s.validate_name()
    s.validate_mark()
    s.calculate_grade()
except ValueError as e:
    print(e)
    
    
