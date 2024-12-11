user=input("Enter Name:")
l1=[]
l2=[]
char=[]
special=[]
for i in user:
    if i in ("1","2","3","4","5","6","7","8","9","0"):
        l2.append(i)
    else:
        l1.append(i)
for j in l1:
    print(*j,end="")
    if j in ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"):
        char.append(j)
    elif j in ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"):
        char.append(j)
    else:
        special.append(j)

print("\n")

for a in char:
    print(*a,end="")

print("\n")
for b in special:
    print(*b,end="")

