#Write a program to put even and odd elements of array in two separate arrays
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b=[]
c=[]
for i in A:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
        
print("Even elements in the array:", b)
print("Odd elements in the array:", c)