#This code takes user input in the form of a number and then uses conditional statements (if, elif, else) 
#to determine and print a message based on the value of the entered number. 

user_number = int(input("Please enter your number between 100 and 200: "))

if user_number < 100:
    print("Less than 100")
elif 100 <= user_number <= 200:
    print("Between 100 and 200")
elif user_number > 200:
    print("Greater than 200")
