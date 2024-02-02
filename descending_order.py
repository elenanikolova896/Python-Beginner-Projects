def descending_order(num):
    digits = [int(digit) for digit in str(num)]
    sorted_digits = sorted(digits, reverse=True)
    result = int(''.join(map(str, sorted_digits)))
    return result

print(descending_order(0))
print(descending_order(15))
print(descending_order(123456789))
