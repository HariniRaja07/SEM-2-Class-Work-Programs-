class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age

name=input("Enter yout name:")
age=int(input("Enter yout name:"))
s=Student(name,age)
n=input()
a=int(input())
s.set_name(n)
s.set_age(a)
print(f"Name:{s.get_name()}\nAge:{s.get_age()}")
