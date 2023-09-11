#This program accepts a "car_prices" dictionary. It iterates through the keys (car models) and values (car prices) in that dictionary and prints them out in a string.

def car_listing(car_prices):
    for car, price in car_prices.items():
        print("A {} costs {} dollars".format(car, price))

print(car_listing({"Kia Soul": 19000, "Lamborghini Diablo": 55000, "Ford Fiesta": 13000, "Toyota Prius": 24000}))
