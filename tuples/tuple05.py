n = int(input("Enter the number of elements in the tuple: "))
print("total number of elements:", n)
if n % 2 == 0:
    print("The number of elements is even")
else:
    print("The number of elements is odd")
print("maximum element:", max(n))
print("minimum element:", min(n))
print("sum of elements:", sum(n))