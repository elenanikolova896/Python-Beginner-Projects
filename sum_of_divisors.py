#This code uses a while loop to calculate the sum of all divisors of a given number, excluding the number itself

def sum_of_divisors(number):
    divisor = 1
    total = 0
    
    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1
        
    return total

input_number = int(input("Enter a number: "))
result = sum_of_divisors(input_number)
print("Sum of divisors of", input_number, "is:", result)
