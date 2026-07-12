#Write a program to count total number of negative elements in an array.

A = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

negative = 0

for num in A:
    if num < 0:
        negative += 1

print("Total number of negative elements:", negative)