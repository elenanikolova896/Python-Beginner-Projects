#This program uses the format method to return first_name and the first initial of last_name followed by a period. 

def nametag(first_name, last_name):
    return "{} {}.".format(first_name, last_name[0])

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
result = nametag(first_name, last_name)
print(result)
