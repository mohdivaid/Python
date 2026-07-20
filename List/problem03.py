#take 5 no as input from user and store them in a list print total no. - sum - max - min.
a = []

for i in range(5):
    num = int(input("Enter a number: "))
    a.append(num)
print(a)
print("Total numbers:", len(a))
print("Sum:", sum(a))
print("Maximum:", max(a))
print("Minimum:", min(a))