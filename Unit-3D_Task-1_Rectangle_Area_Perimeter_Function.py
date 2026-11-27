#to calculate the area and perimeter of a rectangle (length and breadth as parameters) and returns both values
def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area, perimeter = rectangle(length, breadth)
print("Area =", area)
print("Perimeter =", perimeter)
