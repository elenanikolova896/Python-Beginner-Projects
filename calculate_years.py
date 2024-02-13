# Writing down the numbers
def calculate_years(params, years=0):
    # Unpack the parameters
    principal, interest_rate, tax_rate, desired_sum = params

    while principal < desired_sum:
        # Calculate interest, deduct taxes, and update principal for the next year
        principal = principal + principal * interest_rate * (1 - tax_rate)
        # Increment the number of years
        years += 1

    return years

# Example usage:
result = calculate_years((1000, 0.05, 0.18, 1100))
print(result)  # Output: 3
