# After the user makes a choice, the program will redirect
# them to three types of calculators: one for the area of
# a triangle, another for the area of a square, and the
# last one for the area of a pentagon.

calc_choice = input("What would you like to calculate? (triangle, square, pentagon): ")

if calc_choice == "triangle":
    print("To find the area of a triangle, you need the base and height.")

    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    area = 0.5 * base * height
    print("The area of the triangle is \033[31m{:.2f}\033[m".format(area))

elif calc_choice == "square":
    print("To find the area of a square, you need the length of one of its sides.")

    side = float(input("Enter the length of a side of the square: "))

    area = side * side
    print("The area of the square is \033[31m{:.2f}\033[m".format(area))

elif calc_choice == "pentagon":
    print("To find the area of a pentagon, you need the apothem and the side length.")

    apothem = float(input("Enter the apothem of the pentagon: "))
    side = float(input("Enter the side length of the pentagon: "))

    area = 0.5 * apothem * 5 * side
    print("The area of the pentagon is \033[31m{:.2f}\033[m".format(area))