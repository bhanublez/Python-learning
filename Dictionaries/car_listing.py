def car_listing(car_prices):
    result = ""
    for car, price in car_prices.items():
        result += f"{car} costs {price} dollars\n"
    return result

print(car_listing({"Kia Soul": 19000, "Lamborghini Diablo": 55000, "Ford Fiesta": 13000, "Toyota Prius": 24000}))

# Should print:
# A Kia Soul costs 19000 dollars
# A Lamborghini Diablo costs 55000 dollars
# A Ford Fiesta costs 13000 dollars
# A Toyota Prius costs 24000 dollars

car_make="Lamborghini"
print(car_make[3:-5])
print(car_make[-4:])
print(car_make[:7])
# colors = ["red", "white", "blue"]
# colors.insert(2, "yellow")
# print(colors)
# speed_limits = {"street":32}
# print(speed_limits["street"])