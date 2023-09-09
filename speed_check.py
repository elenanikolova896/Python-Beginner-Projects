#This code takes a user-entered speed value (presumably in some unit of measurement) and uses a series of conditional statements 
#to categorize the speed into different levels and then prints an appropriate message. 

speed = float(input("Please enter what is the speed?"))

if speed <= 10:
    print("Slow")

elif 10 < speed <= 50:
    print("Average")

elif 50 < speed <= 150:
    print("Fast")

elif 150 < speed <= 1000:
    print("Ultra fast")

else:
    print("Extremely fast")
