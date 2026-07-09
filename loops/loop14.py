#Write a program to print all Prime numbers between 1 to n.
n = 10
for num in range(1, n + 1):
    prime = True
    
    for i in range(2, int(num // 2) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)