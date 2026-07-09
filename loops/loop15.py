#Write a program to find sum of all prime numbers between 1 to n.
n = 10
sum = 0

for num in range(2, n + 1):
    prime = True
    for i in range(2, int(num // 2) + 1):
        
        if num % i == 0:
            prime = False 
            
    if prime:
        sum += num
        
print("Sum of all prime numbers between 1 to n:", sum)