# To find the largest number in a series of N numbers entered by the user using for loop
total_number = int(input("Enter the total numbers: "))
number = float(input("Enter the number: "))
for count in range(total_number):
    num = float(input("Enter number: "))
    if num > number:
        number = num
print(f"largest among {total_number} numbers is {number}")