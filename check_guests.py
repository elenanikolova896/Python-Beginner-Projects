#the "check_guests" function retrieves the number of guests (value) the specified friend "gues" (key) is bringing and prints the amount of guests

def check_guests(guest_list, guest):
    if guest in guest_list:
        print(guest_list[guest])
    else:
        print("Guest not found.")

guest_list = {
    "Tessa": 5,
    "Rick": 3,
    "Anna": 2,
    "Jake": 4
}

check_guests(guest_list, "Tessa")  # Should print 5
check_guests(guest_list, "Anna")   # Should print 2
check_guests(guest_list, "John")   # Will not print anything for "John"
