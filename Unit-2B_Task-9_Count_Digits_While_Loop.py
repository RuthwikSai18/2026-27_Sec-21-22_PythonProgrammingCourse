#Implement a Python program to count the number of digits in a number using while loop
n = int(input("enter the number: "))

count= 0

while n > 0:
    n = n // 10
    count = count + 1
    
print(count)
