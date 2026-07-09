#Write a program to check whether a number is armStrong number or not
a = 153
sum = 0
temp = a

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp=temp// 10

if sum == a:
    print("a is an Armstrong number.")
else:
    print("a is not an Armstrong number.")