#write a program to check whether a number is prime or not

x=12

prime=True

if x>=1:
    for i in range(2,x):
        if x%i==0:
            prime=False
            
    if prime:
        print("x is a prime number")
    else:
        print("x is not a prime number")
else:
    print("number is negative or zero")