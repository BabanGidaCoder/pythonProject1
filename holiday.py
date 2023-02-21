# The program below takes in input about holiday costs and returns the total costs of the holiday including hotels,
# air ticket and car rental

def hotel_cost(nights, price):
    total_hotel = (nights * price)
    return total_hotel


nights = int(input('Number of nights stay:'))
price = int(input("Enter the price per night of hotel:"))
print(hotel_cost(nights, price))


def plane_cost(city, ):
    city = input("Enter the city you are traveling to:")
    if city == "london":
        return 150
    elif city == "New York":
        return 120
    elif city == "south africa":

        return 190
    else:
        return "invalid city"


print(plane_cost("london"))


# code below calculates the car rental costs based number of days hired

def car_rental(days, ):
    car_rental_cost = (days * 27)

    return car_rental_cost


days = int(input("Enter number of days car hired:"))

print(car_rental(5))


# code below calculates the total price of the holiday taking all three arguments and returns the cost

def holiday_cost(no_nights, city_dest, days_hire):
    no_nights = hotel_cost('', 15)
    city_dest = plane_cost()
    days_hire = car_rental()

    total_cost = (no_nights + city_dest + days_hire)
    return total_cost


print("The total cost for your holiday is :", holiday_cost(3, "london", 3))

