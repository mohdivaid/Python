#Write a program to count total number of duplicate elements in an array.
A = [1, 2, 3, 4, 1, 5, 4, 1]

B = 0

for element in A:
    
    if A.count(element) > 1:
        B += 1

print("Total number of duplicate elements:", B)