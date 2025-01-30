# A program that reads the number of apples purchased, calculates,
# and prints the total purchase amount. 
# NOTE: Each apple costs €0.30, and from 12 units onwards, each costs €0.25.

apples_qty = int(input("Enter the number of apples purchased: "))

if apples_qty < 12:
    total_price = apples_qty * 0.30

else:
    total_price = apples_qty * 0.25

print(f"The total purchase amount is: €{total_price:.2f}")
