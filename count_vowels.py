def count_vowels(input_str):
    # Initialize a variable to store the count of vowels
    vowel_count = 0

    # Use a for loop to iterate over the characters in the string
    for char in input_str:
        # Check if the character is a vowel (consider both uppercase and lowercase)
        if char.lower() in "aeiou":
            # Increment the vowel count if a vowel is found
            vowel_count += 1

    # Return the final count of vowels
    return vowel_count

# Test the function with different strings
print(count_vowels("hello"))   # Expected output: 2 (e, o)
print(count_vowels("Python"))  # Expected output: 1 (o)
print(count_vowels("xyz"))     # Expected output: 0
