a = [10, -5, 0, 20, 32, 0, 8]

l = 0
s = 0

for i in a:
    if i > l:
        l = i
    if i < s:
        s = i
print("largest number:",l)
print("smallest number:",s)