# Q1. Count Even and Odd Numbers

n = [12, 5, 7, 20, 33, 40, 18]

even_count = 0
odd_count = 0

for num in n:
    if num % 2 == 0:
        print(num, "is Even")
        even_count += 1
    else:
        print(num, "is Odd")
        odd_count += 1

print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)