def reverse_string(input_str):
    # Initialize an empty string to store the reversed characters
    reversed_str = ""

    # Use a for loop to iterate over the characters in reverse order
    for char in reversed(input_str):
        # Append each character to the reversed string
        reversed_str += char

    # Return the final reversed string
    return reversed_str

# Test the function with different strings
print(reverse_string("hello"))  # Expected output: "olleh"
print(reverse_string("python"))  # Expected output: "nohtyp"
print(reverse_string(""))        # Expected output: ""
