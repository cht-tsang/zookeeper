# put your python code here
duration = abs(int(input()))
food_cost = abs(int(input()))
flight_cost = abs(int(input()))
hotel_cost = abs(int(input()))

food_total = duration * food_cost
flight_total = flight_cost * 2
hotel_total = hotel_cost * (duration - 1)

vacation_total = food_total + flight_total + hotel_total

print(vacation_total)
