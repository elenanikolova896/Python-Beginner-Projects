#This code calculates the tip amount, total amount to pay, 
#and each person's share of a restaurant bill based on the given bill amount, tip percentage, and the number of friends sharing the bill.

# Given bill amount
bill_amount = 47.28

# Tip percentage
tip_percentage = 15

# Calculate the tip
tip_amount = bill_amount * (tip_percentage / 100)

# Calculate the total amount to pay
total_amount = bill_amount + tip_amount

# Calculate each friend's share
num_friends = 2
each_person_share = total_amount / num_friends

# Output the results
print("Tip amount: ${:.2f}".format(tip_amount))
print("Total amount to pay: ${:.2f}".format(total_amount))
print("Each person needs to pay: ${:.2f}".format(each_person_share))
