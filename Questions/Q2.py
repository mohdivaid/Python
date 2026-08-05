a = [10, -5, 0, 20, -2, 0, 8]

p = 0
z = 0
n = 0

for num in a:
    if num > 0:
        p += 1
    elif num == 0:
        z += 1
    else:
        n += 1

print("Positive:", p)
print("Zero:", z)
print("Negative:", n)