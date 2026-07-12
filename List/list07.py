#Write a program to delete an element from an array at specified position.
A = [1, 2, 3, 4, 5]

position = 2 

if 0 <= position < len(A):
    del A[position]
    print("Array after deletion:", A)
