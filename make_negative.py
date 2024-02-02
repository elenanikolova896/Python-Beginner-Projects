def make_negative(num):
    if num > 0:
        return -num
    elif num == 0:
        return "Error: Zero doesn't have a negative"
    else:
        return num

print(make_negative(4))
print(make_negative(-4))
print(make_negative(0))
