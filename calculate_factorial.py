def calculate_factorial(n):
    if n == 0:
        result = 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
    return result

# Test cases
print(calculate_factorial(0))  # Expected output: 1
print(calculate_factorial(1))  # Expected output: 1
print(calculate_factorial(5))  # Expected output: 120
print(calculate_factorial(10)) # Expected output: 3628800
