#The program receives a string of a house address and formats the address to print it like this: House number ... on a street named ... "

def address_parser(address_string):
    space_index = address_string.find(' ')  # Find the index of the first space
    if space_index != -1:
        house_number = address_string[:space_index]
        street_name = address_string[space_index + 1:]
        return "House number {} on a street named {}".format(house_number, street_name)
    else:
        return "Invalid address format"

input_address = "123 Main Street"
output = address_parser(input_address)
print(output)  # Should print "House number 123 on a street named Main Street"
