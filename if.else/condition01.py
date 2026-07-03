#write a program to find maximum number between three number

a = 10
b = 24
c = 6

if (a>=b and a>=c):
  M = a
elif (b>=a and b>=c):
  M = b
else:
  M = c
print("Maximum number =",M)