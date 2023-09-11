#This program checks if a number between 1 and 6 is even or odd.

for number in range(1, 6):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
