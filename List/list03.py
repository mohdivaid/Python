#Write a program to find second largest element in an array.
A = [1, 2, 3, 4, 5]

a = max(A)
A.remove(a
         )
b = max(A)
print("Second largest element in array:", b)