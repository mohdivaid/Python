# Q3. Word Frequency

words = ["python", "java", "python", "c", "java", "python"]
b = {}

for a in words:
    if a in b:
        b[a] += 1
    else:
        b[a] = 1
        
print(b)