# Write a program to find sum of all even numbers between 1 to n. 
a = 10   
sum = 0
for i in range(1, a + 1):
    if(i%2 == 0):
        sum+=i
    
print("sum of all even numbers:", sum)