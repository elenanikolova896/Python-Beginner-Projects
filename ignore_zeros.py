#This code ignores all 0 numbers in a list of number and prints out all the rest

my_list = [0, 0, 0, 2]

def ignore_zeros():
    for num in my_list:
        if num == 0:
            continue
        print(num)

ignore_zeros()
