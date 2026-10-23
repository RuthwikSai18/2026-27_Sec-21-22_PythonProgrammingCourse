x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
z=int(input("Enter third number: "))
if x>y and x>z:
    print("The largest number is",x)
elif y>x and y>z:
    print("The largest number is",y)
else:
    print("The largest number is",z)