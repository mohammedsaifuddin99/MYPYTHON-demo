#problem 1 : simple Coffe shop order calculator 


Total_bill = 0

coffee_price = 20
tea_price = 15
muffin_price = 25
sandwich_price = 45

coffee_quantity = input("Number of coffees: ")
tea_quantity = input("Number of teas': ")
muffin_quantity = input("Number of muffins: ")
sandwich_quantity = input("Number of sandwiches: ")

coffee_bill = int(coffee_quantity) * coffee_price
tea_bill = int(tea_quantity) * tea_price
muffin_bill = int(muffin_quantity) * muffin_price
sandwich_bill = int(sandwich_quantity) *sandwich_price

Total_bill = coffee_bill + tea_bill + muffin_bill + sandwich_bill

print("____YOUR ORDER____")
print(f"{coffee_quantity} X {coffee_price} = Rs.{coffee_bill}/-")
print(f"{tea_quantity} X {tea_price} = Rs.{tea_bill}/-")
print(f"{muffin_quantity} X {muffin_price} = Rs.{muffin_bill}/-")
print(f"{sandwich_quantity} X {sandwich_price} = Rs.{sandwich_bill}/-")

print(f"Your Total Bill is: Rs. {Total_bill}/-")



# problem 2 : Trip budget calculator

# total_trip_budget = 0
 
# cost_per_litre = 100
# mileage_per_litre = 35
# total_distance = int(input("Total Distance: "))
 
# total_trip_litres =  total_distance / mileage_per_litre
# total_fuel_cost = total_trip_litres * cost_per_litre

# hotel_cost_per_day = 1000
# hotel_stay_days = int(input("Total Stay days: "))
# total_hotel_bill = hotel_stay_days * hotel_cost_per_day
 
# food_budget_per_day = int(input("Food budget per day : "))
# total_eating_days = int(input("Number of eating days: "))
# total_food_budget = total_eating_days * food_budget_per_day
 
# total_activity_budget = int(input("Activities budget: "))
 
# total_trip_budget = total_fuel_cost + total_hotel_bill + total_food_budget + total_activity_budget
 
# print(f"Your total trip budget would be around: Rs. {total_trip_budget} /-")