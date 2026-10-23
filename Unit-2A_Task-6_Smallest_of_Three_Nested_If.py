#Finding the smallest number of the given three numbers
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
z=int(input("Enter the third number: "))
if (x<y) and (x<z):
    smallest=x  
elif (y<x) and (y<z):
    smallest=y
else:
    smallest=z
print("The smallest number is",smallest)