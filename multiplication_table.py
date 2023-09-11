# Python function that generates a multiplication table for a given number while ensuring the result doesn't exceed 25

def multiplication_table(number):
    multiplier = 1
    
    while multiplier <= 5:
        result = number * multiplier
        if result <= 25:
            print(f"{number} x {multiplier} = {result}")
        multiplier += 1

input_number = int(input("Enter a number: "))
multiplication_table(input_number)
