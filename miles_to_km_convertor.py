#This code converts miles to km and calculates also a round-trip.

def convert_distance(miles):
    km = miles * 1.6
    return km

my_trip_miles = 55

# 2) Call the function to convert the trip distance from miles to kilometers.
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion.
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
# and fill in the blank to print the result.
round_trip_km = 2 * my_trip_km
print("The round-trip distance in kilometers is " + str(round_trip_km))
