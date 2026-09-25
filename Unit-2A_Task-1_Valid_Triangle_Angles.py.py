#Three angles forms a valid triangle
Angle_a=int(input("Enter 1st angle:"))
Angle_b=int(input("Enter 2nd angle:"))
Angle_c=int(input("Enter 3rd angle:"))
if Angle_a + Angle_b + Angle_c == 180 and Angle_a > 0 and Angle_b > 0 and Angle_c > 0:
    print(f"The given angles {Angle_a}, {Angle_b}, {Angle_c} is == 180 and froms a valid triangle.")
else :
    print(f"The given angles {Angle_a}, {Angle_b}, {Angle_c} does not forms valid triangle.")