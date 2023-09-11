# This code defines a Python function called sum_positive_numbers that calculates the sum of positive integers from 1 to a given number n using recursion. 

def sum_positive_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_positive_numbers(n - 1)

input_number = int(input("Enter a positive number: "))
if input_number <= 0:
    print("Please enter a positive number.")
else:
    result = sum_positive_numbers(input_number)
    print("Sum of positive numbers from 1 to", input_number, "is:", result)
