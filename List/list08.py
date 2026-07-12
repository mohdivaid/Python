#Write a program to count frequency of each element in an array.
A = [1, 2, 3, 2, 4, 1, 5, 4, 1]

frequency = {}

for element in A:
    frequency[element] = frequency.get(element, 0) + 1

print("Frequency of each element:")

for element, count in frequency.items():
    print(element, "frequency of elements:", count)