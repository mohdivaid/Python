#Write a program to count frequency of each element in an array.
a = [1, 2, 3, 4, 1, 5, 4, 1]

for i in range(len(a)):
    count = 1
    already_counted = False
    
    for j in range(i):
        if a[i] == a[j]:
            already_counted = True
            break
        
    if already_counted:
        continue
    
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            count += 1

    print("Frequency of", a[i], "is:", count)
