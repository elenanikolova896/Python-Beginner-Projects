# function that counts down or up based on the start and stop variables

def counter(start, stop):
    if start > stop:
        print("Counting down:", end=" ")
        for num in range(start, stop - 1, -1):
            print(num, end=", ")
    else:
        print("Counting up:", end=" ")
        for num in range(start, stop + 1):
            print(num, end=", ")
    print()  # Print a new line after counting is done

counter(3, 1)  # Should return "Counting down: 3, 2, 1"
counter(2, 5)  # Should return "Counting up: 2, 3, 4, 5"
