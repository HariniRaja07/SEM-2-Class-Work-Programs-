user=input("Enter First Name:")
l1=[]
l2=[]
for i in user:
    if i in ("1","2","3","4","5","6","7","8","9","0"):
        l2.append(i)
    else:
        l1.append(i)
for j in l1:
    print(*j,end="")

