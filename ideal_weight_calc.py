# A program that reads the gender ('M' for male and 'F' for female)
# and the height in centimeters of a person, then calculates their
# ideal weight using the formula:
# Men [((height / 100) * 78.7) - 58] 
# Women [((height / 100) * 62.1) - 44.7]

sex = input("\nPlease enter 'M' for male or 'F' for female: ")
height = float(input("Please enter your height in centimeters: "))

if sex == 'M':
    ideal_weight = ((height / 100) * 78.7) - 58
    print(f"\nYour ideal weight is {ideal_weight:.2f} kg.")

if sex == 'F':
    ideal_weight = ((height / 100) * 62.1) - 44.7
    print(f"\nYour ideal weight is {ideal_weight:.2f} kg.")

# This program is for learning purposes only and does not represent
# real calculations used by professionals.