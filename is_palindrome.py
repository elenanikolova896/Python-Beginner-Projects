#This program checks if a given string is a palindrome while ignoring blank spaces and capitalization

def is_palindrome(input_string):
    # Remove spaces from input_string and convert to lowercase
    new_string = input_string.replace(" ", "").lower()
    # Create the reverse of the new_string
    reverse_string = new_string[::-1]
    
    # Iterate through each letter of the input string
    for i in range(len(new_string)):
        if new_string[i] != reverse_string[i]:
            return False
    return True

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
