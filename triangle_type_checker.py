# The user provides the 3 side measurements of a triangle,
# and the program informs whether the triangle is
# equilateral, isosceles, or scalene.

size1 = float(input("Enter the first side measurement: "))
size2 = float(input("Enter the second side measurement: "))
size3 = float(input("Enter the third side measurement: "))

if size1 == size2 == size3:
    print("The triangle is equilateral.")

elif size1 == size2 or size1 == size3 or size2 == size3:
    print("The triangle is isosceles.")

else:
    print("The triangle is scalene.")
