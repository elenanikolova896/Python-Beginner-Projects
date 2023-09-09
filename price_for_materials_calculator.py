#This program calculates the total cost of school materials with prices already set. The program also asks for discount percentage and calculates the total cost with discount.

# Prices of materials
pen_price = 5.80
highlighter_price = 7.20
cleaning_detergent_price = 1.20

# Number of packages of pens, highlighters and cleaning detergent student will buy
pens_qty = int(input("Enter the number of packages of pens: "))
highlighters_qty = int(input("Enter the number of packages of highlighters: "))
cleaning_detergent_qty = float(input("Enter the number of liters of cleaning detergent: "))

# Calculate the total cost of materials
total_cost = (pens_qty * pen_price) + (highlighters_qty * highlighter_price) + (cleaning_detergent_qty * cleaning_detergent_price)

# Get the discount percentage
discount = float(input("Enter the discount percentage: "))

# Calculate the total cost after discount
total_cost_with_discount = total_cost - (total_cost * (discount/100))

# Print the final cost
print("Total cost: ", total_cost_with_discount)
