#Begginer
#1.Write a Python program to check if a number is even or odd.
num=int(input())
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")

#2.Write a program to find the largest of three numbers.
n1=int(input())
n2=int(input())
n3=int(input())
if n1>n2 and n1>n3:
    print(f"The Number {n1} is the Largest number")
elif n2>n1 and n2>n3:
    print(f"The Number {n2} is the Largest number")
else:
    print(f"The Number {n3} is the Largest number")


#3.Write a Python program to print the multiplication table of a given number.
num=int(input())
for i in range(1,11):
    print(num,"x",i,"=",i*num)

#4.Write a program to check if a string is a palindrome.
user=input("Enter string:")
rev=user[::-1]
print(rev)
if rev==user:
    print("Yes, It is a palindrome")
else:
    print("No, It is not a palindrome")
    
#5.Write a Python program to calculate the sum of all numbers in a list.
list1=list(map(int,input().split()))
print(sum(list1))

list1=[]
num=int(input())
s=0
for i in range(num):
    list1.append(int(input()))
for i in list1:
    s+=i
print("The sum of the list is:",s)

#6. to count the occurance of letters in a string
#method1
from collections import Counter

string = input("Enter a string: ")
frequency = Counter(string)

print("Character frequencies:")
for char, count in frequency.items():
    print(f"{char}: {count}")


#method2
string = input("Enter a string: ")
frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequencies:")
for char, count in frequency.items():
    print(f"{char}: {count}")


#8.Write a program to reverse a string without using built-in functions.
text=input()
print(text[::-1])

#9.Write a program to find the factorial of a number with using recursion.
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter a number:"))
print(f"The factorial of the number is:{factorial(num)}")

#10.Write a program to find the factorial of a number without using recursion.
num=int(input("Enter a number:"))
factorial=1
for i in range(1,num+1):
    factorial*=i
print(f"The Factorial of the number {num} is : {factorial}")

