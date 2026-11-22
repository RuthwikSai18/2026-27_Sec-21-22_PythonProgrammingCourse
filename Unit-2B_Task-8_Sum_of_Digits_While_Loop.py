#Implement a Python program to find the sum of digits of a number using while loop
n = int(input("Enter the number: "))
sum = 0
while n > 0:
    count = n % 10
    sum = sum + count
    n = n//10
print(sum)
