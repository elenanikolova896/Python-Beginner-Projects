#This program takes a string and prints the first character of the string.

def first_character(input_string):
    return input_string[0]

input_string = input("Enter a string: ")
result = first_character(input_string)
print("The first character is:", result)
