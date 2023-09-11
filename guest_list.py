#The guest_list function reads in a list of tuples with the name, age and profession of each party guest, and prints the sentence
# "Guest is X years old and works as ... ". for each one.

def guest_list(*guests):
    for guest in guests:
        name, age, profession = guest
        print("{} is {} years old and works as a {}.".format(name, age, profession))

guest_list(("Ken", 30, "Chef"), ("Pat", 35, "Lawyer"))
