#Write a program to find frequency of each digit in a given integer.
n = 12321

a = str(n)

for digit in set(a):
    
    print(f"Frequency of {digit} is: {a.count(digit)}")