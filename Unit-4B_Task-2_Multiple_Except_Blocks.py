list_data = [10, 20, 30]
try:
    index = int(input("Enter index: "))
    value = list_data[index]
    print("Value:", value)
except ValueError:  # ValueError — non-integer input
    print("Please enter a valid integer index.")
except IndexError:  # IndexError — index out of range
    print("Index is out of range.")