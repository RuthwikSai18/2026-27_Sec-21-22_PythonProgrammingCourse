total_input_numbers=int(input("Enter how many numbers: "))
total_sum=0
for input_number in range(total_input_numbers):
    number=int(input("Enter a number: "))
    total_sum=total_sum+number
average=total_sum/total_input_numbers
print(f"sum={total_sum}")
print(f"average={average}")