# A program that reads three integer values and returns them in ascending order.

val_one = int(input("Enter the first integer: "))
val_two = int(input("Enter the second integer: "))
val_three = int(input("Enter the third integer: "))

format_string = '\n{}, {}, {}.'

if val_one >= val_two and val_two >= val_three:
    print(format_string.format(val_three, val_two, val_one))

elif val_two >= val_one and val_one >= val_three:
    print(format_string.format(val_three, val_one, val_two))

elif val_three >= val_one and val_one >= val_two:
    print(format_string.format(val_two, val_one, val_three))

elif val_one >= val_three and val_three >= val_two:
    print(format_string.format(val_two, val_three, val_one))

elif val_two >= val_three and val_three >= val_one:
    print(format_string.format(val_one, val_three, val_two))

else:
    print(format_string.format(val_one, val_two, val_three))
