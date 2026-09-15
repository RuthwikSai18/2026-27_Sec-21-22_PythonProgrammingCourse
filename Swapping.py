#Swapping Two numbers
a=int(input("Enter the number(a):"))
b=int(input("Enter the number(b):"))
print(f"before swapping a and b : {a} and {b}")
a=a+b
b=a-b
a=a-b
print(f"After swapping a and b: {a} and {b}")