class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages

b1=Book(400)
b2=Book(300)

print("Total number of pages:",b1+b2)




class Addition:
    def add(self,a,b,c=0):
        result=0
        result=a+b+c
        return result

a=aAddition()
ans=a.add(2,3)
print(ans)
ans1=a.add(2,3,4)
print(ans1)
