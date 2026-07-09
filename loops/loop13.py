#Write a program to calculate factorial of a number.

n = 3

factorial = 1
for i in range(1, n + 1):
    
    factorial *= i
    
print("Factorial of n:", factorial)