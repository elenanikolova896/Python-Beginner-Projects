#This code calculates the total cost of repainting a living room, considering the prices and quantity of materials 
#provided by the user, including nylon, paint, paint weakener and cost of worker.

# Prices for repainting the living room
nylon_for_sqmeter = 1.50
paint_for_liter = 14.50
paint_weakner_for_liter = 5.00

# Quantity of materials
nylon = int(input("How many square meters of nylon do you need?"))
paint = int(input("How many liters of paint do you need?"))
paint_weakner = int(input("How many liters of paint weakner do you need?"))

# Total sum of materials calculation
nylon_sum = (nylon + 2) * nylon_for_sqmeter
paint_sum = paint + (paint * 10/100) * paint_for_liter
paint_weakner_sum = paint_weakner * paint_weakner_for_liter
packages = 0.40
total_sum_for_materials = nylon_sum + paint_sum + paint_weakner_sum + packages

sum_for_workers_per_hour = total_sum_for_materials * (total_sum_for_materials * (30/100) )
hours_of_work = int(input("How many hours will the workers need to pain the living room?"))
total_sum_for_workers = hours_of_work * sum_for_workers_per_hour

total_amount_of_everything = total_sum_for_materials + total_sum_for_workers

print(total_amount_of_everything)
