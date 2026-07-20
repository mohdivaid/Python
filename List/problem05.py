#remove 20 all in list and print the list and print how many time 20 occurs.

a = [10, 20, 30, 40, 20, 50, 20]
count = a.count(20)
while 20 in a:
    a.remove(20)
print("List after removing all 20:", a)
print("Number of times 20 occurs:", count)