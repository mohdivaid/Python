a = []

for i in range(10):
    
    num = int(input("Enter number: ",))
    
    if num % 2 == 0:
        a.append(num)

print("Even numbers list:", a)