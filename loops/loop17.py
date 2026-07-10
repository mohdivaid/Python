#Write a program to print all Strong numbers between 1 to n.
    
a = 153

for i in range(1, a + 1):
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit**3
        temp //= 10
    if i==sum:
        print(i)


 

