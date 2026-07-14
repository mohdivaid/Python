#Write a program to count total number of duplicate elements in an array.
A = [1, 2, 3, 4, 1, 5, 4, 1]

b = []            

for i in range (len(a)):
    for j in range(i + 1, len(a)):  
        if a[i] == a[j] and a[i] not in b:       
                
                b.append(a[i])

print("Duplicate elements:", b)
