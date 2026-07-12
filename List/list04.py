#Write a program to count total number of even and odd elements in an array.
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

even= 0
odd= 0

for num in A:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Total number of even elements:", even)
print("Total number of odd elements:", odd)