# Write a program to find sum of all odd numbers between 1 to n. 

sum = 0
for i in range(1, 11):
    
    if(i%2 != 0):
        sum+=i
    
print(sum)