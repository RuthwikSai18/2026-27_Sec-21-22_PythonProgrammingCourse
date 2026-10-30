# Write a python program to print the multiplication table of a number using for loop
n=int(input("Enter a number: "))
for i in range(1, 11):
    print(n, 'x', i, '=', n*i)
# Write a python program to print the multiplication table of a number using while loop
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n, 'x', i, '=', n*i)
    i = i + 1