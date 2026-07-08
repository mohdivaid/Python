#Write a program to calculate sum of digits of a number.
a = 98765
sum = 0

for digit in str(a):
    sum += int(digit)
    
print("Sum of digits:", sum)
