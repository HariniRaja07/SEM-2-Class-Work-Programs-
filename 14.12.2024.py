#1
def Merge(word1, word2):
    l1= []
    i=0
    j=0
    while i < len(word1) and j < len(word2):
        l1.append(word1[i])
        l1.append(word2[j])
        i += 1
        j += 1
        l1.append(word1[i:])
        l1.append(word2[j:])
        return ''.join(l1)
word1=input()
word2=input()
output = Merge(word1, word2)
print(output)

#2
def Flowers(flowerbed, n): 
    for i in range(len(flowerbed)): 
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0): 
            flowerbed[i] = 1 
            n -= 1 
            if n == 0: 
                return True 
    return False 

flowerbed = [1, 0, 0, 0, 1] 
n = int(input("Enter the number of flowers to plant: ")) 
print(Flowers(flowerbed, n))
