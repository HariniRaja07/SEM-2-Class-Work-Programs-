#3.
n=int(input())
list1=[]
for i in range(n):
    list1.append(int(input()))
print(sum(list1))


#4.
L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
for i in L1:
    if i in L2:
        print("Common elements:",i)

#2
n=int(input())
list1=[]
for i in range(n):
    list1.append(int(input()))
print(list1)
set1=set(list1)
print(set1)
list1=list(set1)
print(list1[::-1])
